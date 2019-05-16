import os
import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_uploader import DeliveryRequestUploader
from model.firebase.bucket import Bucket
from tests import utils


class UploaderTest(unittest.TestCase):
    def test_upload(self):
        request = utils.create_delivery_request()

        DeliveryRequestUploader.upload(request)

    def test_get_invalid_url_should_return_empty_string(self):
        something = Bucket.get_url("some_invalid_url")
        self.assertIsNone(something)
        something = Bucket.get_url(45)
        self.assertIsNone(something)
