from google.cloud import firestore as fs  # type: ignore
from google.auth.credentials import Credentials
from google.auth import _helpers
from kivy.app import App

from model.firebase.firebase import Firebase
from model.firebase.firestore import Firestore
from kivy.storage.jsonstore import JsonStore
import requests
import json

credential_store = JsonStore('credentials.json')

webApiKey = "AIzaSyAZyHcBO03Pf9RK0eM3ifYErGG8eP57aTA"  # Web Api Key

class Auth:
    @staticmethod
    def sign_in_with_tokens(id_token, refresh_token):
        credentials = FirebaseCredentials(token=id_token,
                                          refresh_token=refresh_token)
        Firebase.db = fs.Client(project="carrepsa", credentials=credentials)
        app = App.get_running_app()
        app.is_authenticated = True

    @staticmethod
    def sign_in(email, password):
        """Authenticate the user to firebase"""
        sign_in_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + webApiKey
        sign_in_payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        sign_in_request = requests.post(sign_in_url, data=sign_in_payload)
        sign_in_data = json.loads(sign_in_request.content.decode())

        if sign_in_request.ok == True:
            id_token = sign_in_data['idToken']
            refresh_token = sign_in_data['refreshToken']
            credential_store.put('tokens', id_token=id_token, refresh_token=refresh_token)
            Auth.sign_in_with_tokens(id_token, refresh_token)

            return True

        return False

    @staticmethod
    def sign_up(email, password, name, phonenumber):
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + webApiKey
        signup_payload = {"email": email, "password": password, "returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        sign_up_data = json.loads(sign_up_request.content.decode())

        if sign_up_request.ok == True:
            token = sign_up_data['idToken']
            refresh_token = sign_up_data['refreshToken']
            uid = sign_up_data['localId']

            Auth.sign_in_with_tokens(token, refresh_token)

            batch = Firestore.batch("users")
            batch.set(uid, {"email": email, "name": name, "phonenumber": phonenumber})
            batch.commit()

            print("done")

        elif sign_up_request.ok == False:
            error_data = json.loads(sign_up_request.content.decode())
            error_message = error_data["error"]['message']
            print(error_data)
            print(error_message)
            if error_message == "EMAIL_EXISTS":
                print("finns redan denna mail")


class FirebaseCredentials(Credentials):
    """Firebase Credentials, stores the authentication tokens"""
    token = None
    refresh_token = None

    def __init__(self, token, refresh_token):
        super().__init__()
        self.token = token
        self.refresh_token = refresh_token

    def apply(self, headers, token=None):
        """Apply the token to the authentication header.

        Args:
            headers (Mapping): The HTTP request headers.
            token (Optional[str]): If specified, overrides the current access
                token.
        """

        headers['authorization'] = 'Bearer {}'.format(
            _helpers.from_bytes(self.token))

    def refresh(self, request):
        print("nah")