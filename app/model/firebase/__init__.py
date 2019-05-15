from google.cloud import firestore as fs, storage  # type: ignore

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    _db = None
    _bucket = None

    @staticmethod
    def get_db():
        """Fetch the common firebase db instance."""
        if not hasattr(Firebase, "_db"):
            Firebase._db = fs.Client()

        return Firebase._db

    @staticmethod
    def get_bucket() -> storage.Bucket:
        """Fetch the common firebase storage bucket instance"""
        if not hasattr(Firebase, "_bucket"):
            Firebase._bucket = storage.Client().get_bucket(
                "carrepsa.appspot.com")

        return Firebase._bucket
