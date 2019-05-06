from google.cloud import firestore  # type: ignore

import os

from google.cloud.firestore_v1 import Client

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db instance."""

    db = firestore.Client()

    @staticmethod
    def get_db() -> Client:
        """Fetch the common firebase db instance."""
        return Firebase.db
