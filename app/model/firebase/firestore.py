from model.firebase import Firebase


class Firestore:
    @staticmethod
    def subscribe(path, callback):
        Firestore.refs[path] = Firebase.get_db().collection(path)
        Firestore.refs[path].on_snapshot(callback)

    @staticmethod
    def unsubscribe(path):
        Firestore.refs[path].unsubscribe()

    @staticmethod
    def batch(path):
        return FirestoreBatch(Firestore.db.batch(),
                              Firestore.db.collection(path))


class FirestoreBatch:
    batchRef = None
    collection = None

    def __init__(self, batchRef, collection):
        self.batchRef = batchRef
        self.collection = collection

    #Undrar du också vilken av create, set och update du ska använda?
    #https://googleapis.github.io/google-cloud-python/latest/firestore/batch.html

    def create(self, document, dict):
        self.batchRef.create(self.collection.document(document), dict)

    def set(self, document, dict, merge=False):
        self.batchRef.set(self.collection.document(document), dict, merge)

    def update(self, document, updated_dict):
        self.batchRef.update(self.collection.document(document), updated_dict)

    def delete(self, document):
        self.batchRef.delete(self.collection.document(document))

    def commit(self):
        self.batchRef.commit()


Firestore.refs = {}
