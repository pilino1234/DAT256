import os
import string
import unittest

from model.firebase.auth import Auth
from model.firebase.bucket import Bucket


class BucketTest(unittest.TestCase):
    def setUp(self) -> None:
        mail = os.environ['CARREPSA_CI_EMAIL']
        password = os.environ['CARREPSA_CI_PASS']

        Auth.sign_in(mail, password)

    def test_auto_id(self):
        auto = Bucket._auto_id()

        self.assertEqual(len(auto), 20)

        allowed_characters = string.ascii_letters + string.digits
        self.assertTrue(all(letter in allowed_characters for letter in auto))

    @unittest.skipUnless(os.path.exists("assets/jigglypuff.png"), "Could not find assets for test")
    def test_upload_download_get_url_and_delete(self):
        jigglypuff_blob_name = Bucket.upload("assets/jigglypuff.png")
        self.assertIsNotNone(jigglypuff_blob_name)

        jigglypuff_string = Bucket.download_as_string(jigglypuff_blob_name)
        self.assertGreater(len(jigglypuff_string), 200)

        jigglypuff_url = Bucket.get_url(jigglypuff_blob_name)
        self.assertIsInstance(jigglypuff_url, str)

        Bucket.delete(jigglypuff_blob_name)

        # Try to get image after deletion, expect no result
        new_url = Bucket.get_url(jigglypuff_blob_name)
        self.assertIsNone(new_url)

        new_string = Bucket.download_as_string(jigglypuff_blob_name)
        self.assertIsNone(new_string)

    def test_get_invalid_url_should_return_none(self):
        something = Bucket.get_url("some_invalid_url")
        self.assertIsNone(something)

        something = Bucket.get_url(45)
        self.assertIsNone(something)
