from google.cloud import firestore, storage  # type: ignore

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    db = firestore.Client()
    bucket = storage.Client().get_bucket("carrepsa.appspot.com")

    @staticmethod
    def get_db():
        """Fetch the common firebase db instance."""
        return Firebase.db

    @staticmethod
    def get_bucket() -> storage.Bucket:
        """Fetch the common firebase storage bucket instance"""
        return Firebase.bucket
