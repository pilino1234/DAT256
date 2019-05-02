from google.cloud import firestore
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keyfile.json"


class Firebase:
    @staticmethod
    def get_db():
        return Firebase.db


Firebase.db = firestore.Client()
