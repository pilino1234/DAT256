import random
import string

from model.firebase import Firebase

from typing import Optional


_AUTO_ID_CHARS = string.ascii_letters + string.digits

class Bucket:
    """Carrepsa Cloud Storage Bucket interface"""

    @staticmethod
    def delete(path: str):
        """Deletes a file from Firebase Storage"""
        blob = Firebase.bucket.get_blob(path)
        blob.delete()

    @staticmethod
    def download(path: str) -> Optional[str]:
        """Downloads file from Firebase Storage"""
        blob = Firebase.bucket.get_blob(path)
        if blob is None:
            return None
        return blob.download_as_string()

    @staticmethod
    def upload(path_to_file: str):
        """Uploads from a file on the system"""
        file_extension = path_to_file.split(".")[-1]
        blob = Firebase.bucket.blob(Bucket._auto_id() + "/img." +
                                    file_extension)
        blob.upload_from_filename(path_to_file)

    @staticmethod
    def _auto_id():
        """Generate a "random" automatically generated ID.

        Returns:
            str: A 20 character string composed of digits, uppercase and
            lowercase and letters.
        """
        return "".join(random.choice(_AUTO_ID_CHARS) for _ in range(20))
