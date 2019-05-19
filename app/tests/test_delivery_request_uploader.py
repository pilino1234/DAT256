import os
import unittest

from model.delivery_request_uploader import DeliveryRequestUploader
from model.firebase import Auth
from model.firebase.bucket import Bucket
from model.firebase.firebase import Firebase
from tests import utils


class UploaderTest(unittest.TestCase):
    def setUp(self) -> None:
        mail = os.environ['CARREPSA_CI_EMAIL']   # TODO: travis@carrepsa.ci
        password = os.environ['CARREPSA_CI_PASS']   # TODO: CIrrepsa

        Auth.sign_in(mail, password)

    def test_upload(self):
        request = utils.create_delivery_request()

        DeliveryRequestUploader.upload(request)

    def test_get_invalid_url_should_return_empty_string(self):
        something = Bucket.get_url("some_invalid_url")
        self.assertIsNone(something)
        something = Bucket.get_url(45)
        self.assertIsNone(something)
