from google.cloud import firestore as fs, storage  # type: ignore

from google.auth.credentials import Credentials
import requests
import json
import os
from google.auth import _helpers

from google.cloud.storage import Bucket

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"

webApiKey = "AIzaSyAZyHcBO03Pf9RK0eM3ifYErGG8eP57aTA"  # Web Api Key


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    _db = None
    _bucket: Bucket = None

    @staticmethod
    def sign_in(email, password):
        signin_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + webApiKey
        signin_payload = {"email": email, "password": password, "returnSecureToken": True}
        signin_request = requests.post(signin_url, data=signin_payload)
        sign_in_data = json.loads(signin_request.content.decode())

        if signin_request.ok == True:
            refresh_token = sign_in_data['refreshToken']
            localId = sign_in_data['localId']
            idToken = sign_in_data['idToken']

            print(idToken)

            credentials = FirebaseCredentials(token=idToken, refresh_token=refresh_token)

            Firebase._db = fs.Client(credentials=credentials)

            # print(Firebase.db.collection("packages").get())

    # elif signin_request.ok == False:
    #     error_data = json.loads(signin_request.content.decode())
    #     error_message = error_data["error"]['message']
    #     app.root.ids['login_screen'].ids['login_message'].text = "EMAIL EXISTS - " + error_message.replace("_", " ")

    @staticmethod
    def get_db() -> fs.Client:
        """Fetch the common firebase db instance."""
        return Firebase._db

    @staticmethod
    def get_bucket() -> storage.Bucket:
        """Fetch the common firebase storage bucket instance"""
        if Firebase._bucket is None:
            Firebase._bucket = storage.Client().get_bucket(
                "carrepsa.appspot.com")

        return Firebase._bucket

class FirebaseCredentials(Credentials):
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

Firebase.sign_in("portalsasdf@chalmers.it", "asdfasdf")
