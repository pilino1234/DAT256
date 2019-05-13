from typing import Callable, Dict

from google.cloud.firestore_v1.batch import WriteBatch
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference

from model.firebase import Firebase


class Firestore:
    """Carrepsa Cloud Firestore DB interface."""

    refs: Dict[str, CollectionReference] = {}

    @staticmethod
    def subscribe(path: str, callback: Callable):
        """Subscribes to a collection, executing callback whenever the collection is updated."""
        Firestore.refs[path] = Firebase.get_db().collection(path)
        Firestore.refs[path].on_snapshot(callback)

    @staticmethod
    def unsubscribe(path: str):
        """Unsubscribe from a collection."""
        if path in Firestore.refs:
            Firestore.refs[path].unsubscribe()

    @staticmethod
    def batch(path: str):
        """
        Create a batch read/write object.

        This allows modifications of multiple documents in a single commit.
        """
        return _FirestoreBatch(Firebase.get_db().batch(),
                               Firebase.get_db().collection(path))

    @staticmethod
    def get(path: str) -> CollectionReference:
        """
        Fetch all items in a path from the Firestore database

        :param path: The Firestore path of the collection to get
        :type path: str
        :return: An iterable containing the documents in the path.
        """
        return Firebase.get_db().collection(path).get()

    @staticmethod
    def get_raw(path: str):
        """Returns raw collection at a given path in the database"""
        return Firebase.get_db().collection(path)


    class _FirestoreBatch:
        """
        Firestore batch model.

        For more details, see:
        https://googleapis.github.io/google-cloud-python/latest/firestore/batch.html
        """

        _batch_ref: WriteBatch = None
        _collection: CollectionReference = None

        def __init__(self, batch_ref: WriteBatch, collection: CollectionReference):
            """Initializes the batch reference and collection."""
            self._batch_ref = batch_ref
            self._collection = collection

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                self.commit()

        def create(self, document_data: dict):
            """
            Create a document.

            This method generates a random, unique UID for the document.
            """
            self._batch_ref.create(self._collection.document(), document_data)

        def set(self, document: DocumentReference, document_data: dict):
            """Replace document with new document data."""
            self._batch_ref.set(self._collection.document(document), document_data,
                                False)

        def update(self, document: DocumentReference, field_updates: dict):
            """Update existing document with new data."""
            self._batch_ref.update(self._collection.document(document),
                                   field_updates)

        def delete(self, document: DocumentReference):
            """Delete document."""
            self._batch_ref.delete(self._collection.document(document))

        def commit(self):
            """Commit changes."""
            self._batch_ref.commit()
