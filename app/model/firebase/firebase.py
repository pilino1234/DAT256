import os

from google.cloud import firestore as fs, storage  # type: ignore

from model.firebase.firebase_credentials import FirebaseCredentials
from model.firebase.firebase_exception import FirebaseException

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    _db: fs.Client = None
    _bucket: storage.Bucket = None

    @staticmethod
    def get_db() -> fs.Client:
        """Fetch the common firebase db instance."""
        if Firebase._db is None:
            raise FirebaseException(
                "create_db() must be called before get_db()")

        return Firebase._db

    @staticmethod
    def create_db(credentials: FirebaseCredentials, project: str = "carrepsa"):
        """
        Creates the database reference to Firebase
        :param credentials: Credentials that has tokens and refresh_token
        :param project: The Firebase project
        """
        Firebase._db = fs.Client(project=project, credentials=credentials)

    @staticmethod
    def get_bucket() -> storage.Bucket:
        """Fetch the common firebase storage bucket instance"""
        if Firebase._bucket is None:
            raise FirebaseException(
                "create_bucket() must be called before get_bucket()")

        return Firebase._bucket

    @staticmethod
    def create_bucket():
        """Creates bucket reference to Firebase storage"""
        client = storage.Client()
        Firebase._bucket = client.get_bucket("carrepsa.appspot.com")
