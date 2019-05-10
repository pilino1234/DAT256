from model.firebase import Firebase


class Firestore:
    """Carrepsa Cloud Firestore DB interface."""

    refs = dict

    @staticmethod
    def subscribe(path, callback):
        """Subscribes to a collection, executing callback whenever the collection update."""
        Firestore.refs[path] = Firebase.get_db().collection(path)
        Firestore.refs[path].on_snapshot(callback)

    @staticmethod
    def unsubscribe(path):
        """Unsubscribes a collection."""
        Firestore.refs[path].unsubscribe()

    @staticmethod
    def batch(path):
        """
        Creates a FirestoreBatch

        Creates a batch read/write object to allow
        modifications of multiple documents in a single commit.
        """
        return FirestoreBatch(Firebase.get_db().batch(),
                              Firebase.get_db().collection(path))


class FirestoreBatch:
    """
    Firestore batch model.

    For more details, see:
    https://googleapis.github.io/google-cloud-python/latest/firestore/batch.html
    """

    batch_ref = None
    collection = None

    def __init__(self, batch_ref, collection):
        """Initializes the batch reference and collection."""
        self.batch_ref = batch_ref
        self.collection = collection

    def create(self, document, dict):
        """Create a document."""
        self.batch_ref.create(self.collection.document(document), dict)

    def set(self, document, dict, merge=False):
        """Replace document."""
        self.batch_ref.set(self.collection.document(document), dict, merge)

    def update(self, document, updated_dict):
        """Update document."""
        self.batch_ref.update(self.collection.document(document), updated_dict)

    def delete(self, document):
        """Delete document."""
        self.batch_ref.delete(self.collection.document(document))

    def commit(self):
        """Commit changes."""
        self.batch_ref.commit()
