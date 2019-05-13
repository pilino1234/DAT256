
from google.cloud import firestore as fs, storage  # type: ignore

webApiKey = "AIzaSyAZyHcBO03Pf9RK0eM3ifYErGG8eP57aTA"  # Web Api Key

class Firebase:
    """Stores the common firebase db and storage bucket instance."""

    _db = None
    _bucket = None

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
