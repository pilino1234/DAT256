from google.cloud import firestore  # type: ignore

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db instance."""

    db = firestore.Client()

    @staticmethod
    def get_db():
        """Fetch the common firebase db instance."""
        return Firebase.db
