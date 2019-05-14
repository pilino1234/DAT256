import unittest

from model.firebase.bucket import Bucket


class BucketTest(unittest.TestCase):
    def test_uploading(self):
        jigglypuff_blob_name = Bucket.upload("app/assets/jigglypuff.png")
        self.assertIsNotNone(jigglypuff_blob_name)
        jigglypuff_string = Bucket.download_as_string(jigglypuff_blob_name)
        self.assertGreater(len(jigglypuff_string), 200)
        jigglypuff_url = Bucket.get_url(jigglypuff_blob_name)
        self.assertIsInstance(jigglypuff_url, str)
        Bucket.delete(jigglypuff_blob_name)
        # Try to get image after deletion, expect exception
        new_url = Bucket.get_url(jigglypuff_blob_name)
        self.assertIsNone(new_url)
        new_string = Bucket.download_as_string(jigglypuff_blob_name)
        self.assertIsNone(new_url)
