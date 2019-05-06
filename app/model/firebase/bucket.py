from model.firebase import Firebase


class Bucket:
    """Carrepsa Cloud Storage Bucket interface"""

    @staticmethod
    def delete(path: str):
        """Deletes a file from Firebase Storage"""
        blob = Firebase.bucket.get_blob(path)
        blob.delete()

    @staticmethod
    def download(path: str) -> str:
        """Downloads file from Firebase Storage"""
        blob = Firebase.bucket.get_blob(path)
        if blob is None:
            return ""
        return blob.download_as_string()

    @staticmethod
    def upload(path_to_file: str):
        """Uploads from a file on the system"""
        file_extension = path_to_file.split(".")[-1]
        blob = Firebase.bucket.blob(Firebase.auto_id() + "/img." +
                                    file_extension)
        blob.upload_from_filename(path_to_file)
