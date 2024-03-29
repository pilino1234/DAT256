import datetime
import random
import string

from typing import Optional

from model.firebase.firebase import Firebase

_AUTO_ID_CHARS = string.ascii_letters + string.digits


class Bucket:
    """Carrepsa Cloud Storage Bucket interface"""

    @staticmethod
    def delete(path: str):
        """Deletes a file from Firebase Storage"""
        blob = Firebase.get_bucket().get_blob(path)
        blob.delete()

    @staticmethod
    def download_as_string(path: str) -> Optional[str]:
        """Downloads file from Firebase Storage"""
        blob = Firebase.get_bucket().get_blob(path)
        if blob is None:
            return None
        return blob.download_as_string()

    @staticmethod
    def get_url(blob_name: str) -> Optional[str]:
        """Downloads file from Firebase Storage"""
        try:
            blob = Firebase.get_bucket().get_blob(blob_name)
        except ValueError:
            return None

        if blob is None:
            return None
        return blob.generate_signed_url(datetime.timedelta(seconds=300),
                                        method='GET')

    @staticmethod
    def upload(path_to_file: str):
        """Uploads from a file on the system"""
        file_extension = path_to_file.split(".")[-1]

        blob_name = Bucket._auto_id() + "/img." + file_extension
        blob = Firebase.get_bucket().blob(blob_name)
        blob.upload_from_filename(path_to_file)
        return blob_name

    @staticmethod
    def _auto_id():
        """
        Generate a "random" automatically generated ID.

        Returns
        -------
            str: A 20 character string composed of digits, uppercase and
            lowercase and letters.

        """
        return "".join(random.choice(_AUTO_ID_CHARS) for _ in range(20))
