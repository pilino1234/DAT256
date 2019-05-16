from google.cloud import firestore as fs, storage  # type: ignore

import os

from google.cloud.storage import Bucket

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    _db = None
    _bucket: Bucket = None

    @staticmethod
    def get_db():
        """Fetch the common firebase db instance."""
        if Firebase._db is None:
            Firebase._db = fs.Client()

        return Firebase._db

    @staticmethod
    def get_bucket() -> storage.Bucket:
        """Fetch the common firebase storage bucket instance"""
        if Firebase._bucket is None:
            Firebase._bucket = storage.Client().get_bucket(
                "carrepsa.appspot.com")

        return Firebase._bucket
