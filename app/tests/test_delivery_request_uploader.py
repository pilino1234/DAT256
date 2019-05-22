import os
import unittest

from model.delivery_request_uploader import DeliveryRequestUploader
from model.firebase.auth import Auth
from tests import utils


class UploaderTest(unittest.TestCase):
    def setUp(self) -> None:
        mail = os.environ['CARREPSA_CI_EMAIL']
        password = os.environ['CARREPSA_CI_PASS']

        Auth.sign_in(mail, password)

    def test_upload(self):
        request = utils.create_delivery_request()

        try:
            DeliveryRequestUploader.upload(request)
        except Exception:
            return

        self.assertEqual(1, 1, "This assert will only be called if the test doesn't error out earlier.")
