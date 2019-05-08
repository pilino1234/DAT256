from google.cloud import firestore  # type: ignore

import os

from google.cloud.firestore_v1 import Client

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    """Stores the common firebase db instance."""

    _db: Client

    @staticmethod
    def get_db() -> Client:
        """Fetch the common firebase db instance."""
        if not Firebase._db:
            Firebase._db = firestore.Client()

        return Firebase._db
