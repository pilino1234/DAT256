from model.firebase import Firebase

class Bucket:
    """Carrepsa Cloud Storage Bucket interface"""

    @staticmethod
    def delete(path):
        blob = Firebase.bucket.get_blob(path)
        blob.delete()

    @staticmethod
    def download(path):
        blob = Firebase.bucket.get_blob(path)
        if blob is None:
            return None
        return blob.download_as_string()

    @staticmethod
    def upload(path_to_file):
        file_extension = path_to_file.split(".")[-1]
        blob = Firebase.bucket.blob(Firebase.auto_id() + "/img." + file_extension)
        blob.upload_from_filename(path_to_file)
