from google.cloud import firestore as fs, storage  # type: ignore
from google.auth.credentials import Credentials
import requests
import json
from google.auth import _helpers

webApiKey = "AIzaSyAZyHcBO03Pf9RK0eM3ifYErGG8eP57aTA"  # Web Api Key


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    _db = None
    _bucket: storage.Bucket = None

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
            refresh_token = sign_in_data['refreshToken']
            idToken = sign_in_data['idToken']
            credentials = FirebaseCredentials(token=idToken,
                                              refresh_token=refresh_token)
            Firebase._db = fs.Client(project="carrepsa", credentials=credentials)
            return True

        return False

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

Firebase.sign_in("portalsasdf@chalmers.it", "asdfasdf")
