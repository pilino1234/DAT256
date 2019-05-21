from typing import Callable, Dict, Generator

from google.cloud.firestore_v1.batch import WriteBatch
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference

from model.firebase.firebase import Firebase


class Firestore:
    """Carrepsa Cloud Firestore DB interface."""

    refs: Dict[str, CollectionReference] = {}

    @staticmethod
    def subscribe(path: str, callback: Callable):
        """
        Subscribes to a collection, executing callback whenever the collection is updated.

        Example on a callable function

        def on_snapshot(collection_snapshot, collection_change_snapshot, timestamp):
            for doc in collection_snapshot:
                print(u’{} => {}’.format)(doc.id, doc.to_dict()))

        :param path: Full path to a collection
        :param callback: The function that will be called when an update happens in the collection

        """
        Firestore.refs[path] = Firebase.get_db().collection(path).on_snapshot(
            callback)

    @staticmethod
    def subscribe_document(collection_path: str, document: str,
                           callback: Callable):
        """
        Subscribes to a document, executing callback whenever the collection is updated.

        Example on a callable function

        def on_snapshot(document_snapshot):
            for doc in document_snapshot:
                print(u’{} => {}’.format)(doc.id, doc.to_dict()))

        :param collection_path: The collection, e.g. /users
        :param document: The last bit of the path specifying the document
        :param callback: The function that will be called when an update happens in the document

        """
        path = collection_path + "/" + document
        Firestore.refs[path] = Firebase.get_db().collection(
            collection_path).document(document).on_snapshot(callback)

    @staticmethod
    def unsubscribe(path: str):
        """
        Unsubscribe from a collection.

        :param path: e.g. /users/asdfdfasfsdfdsasfdasdf/packages
        :return:
        """
        if path in Firestore.refs:
            Firestore.refs[path].unsubscribe()

    @staticmethod
    def unsubscribe_document(collection_path: str, document: str):
        """
        Unsubscribe from a document

        :param collection_path: The collection, e.g. /users
        :param document: The last bit of the path specifying the document
        """
        path = collection_path + "/" + document
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
    def get(path: str) -> Generator:
        """
        Fetch all items in a path from the Firestore database

        :param path: The Firestore path of the collection to get
        :type path: str
        :return: An iterable containing the documents in the path.
        """
        return Firebase.get_db().collection(path).stream()

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

    _batchRef: WriteBatch = None
    _collection: CollectionReference = None

    def __init__(self, batch_ref: WriteBatch, collection: CollectionReference):
        """Initializes the batch reference and collection."""
        self._batchRef = batch_ref
        self._collection = collection

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()

    def create_with_random_id(self, document_data: dict):
        """
        Create a document.

        This method generates a random, unique UID for the document.
        """
        document: DocumentReference = self._collection.document()
        self._batchRef.create(document, document_data)
        return document.id

    def create(self, document: DocumentReference, document_data: dict):
        """Create a document."""
        self._batchRef.create(self._collection.document(document),
                              document_data)

    def set(self, document: DocumentReference, document_data: dict):
        """Replace document with new document data."""
        self._batchRef.set(self._collection.document(document), document_data,
                           False)

    def update(self, document: DocumentReference, field_updates: dict):
        """Update existing document with new data."""
        self._batchRef.update(self._collection.document(document),
                              field_updates)

    def delete(self, document: DocumentReference):
        """Delete document."""
        self._batchRef.delete(self._collection.document(document))

    def commit(self):
        """Commit changes."""
        self._batchRef.commit()
