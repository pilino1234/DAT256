from google.cloud import firestore, storage  # type: ignore
from google.cloud.storage.bucket import Bucket as GoogleBucket
import random
import string
import os

_AUTO_ID_CHARS = string.ascii_letters + string.digits

from google.cloud.firestore_v1 import Client

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    db = firestore.Client()
    bucket = storage.Client().get_bucket("carrepsa.appspot.com")

    @staticmethod
    def get_db() -> Client:
        """Fetch the common firebase db instance."""
        return Firebase.db

    @staticmethod
    def get_bucket() -> GoogleBucket:
        """Fetch the common firebase storage bucket instance"""
        return Firebase.bucket

    @staticmethod
    def auto_id() -> str:
        """
        Generate a "random" automatically generated ID.

        Returns
        -------
            str: A 20 character string composed of digits, uppercase and
            lowercase and letters.

        """
        return "".join(random.choice(_AUTO_ID_CHARS) for _ in range(20))
