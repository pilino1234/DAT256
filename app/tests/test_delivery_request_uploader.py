import os
import unittest

from model.delivery_request_uploader import DeliveryRequestUploader
from model.firebase.auth import Auth
from model.firebase.bucket import Bucket
from tests import utils


class UploaderTest(unittest.TestCase):
    def setUp(self) -> None:
        mail = os.environ['CARREPSA_CI_EMAIL']
        password = os.environ['CARREPSA_CI_PASS']

        Auth.sign_in(mail, password)

    def test_upload(self):
        request = utils.create_delivery_request()

        DeliveryRequestUploader.upload(request)  # TODO: add assert

    def test_get_invalid_url_should_return_none(self):
        something = Bucket.get_url("some_invalid_url")
        self.assertIsNone(something)
        something = Bucket.get_url(45)
        self.assertIsNone(something)
