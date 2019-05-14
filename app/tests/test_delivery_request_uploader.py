import os
import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_uploader import DeliveryRequestUploader
from model.firebase.bucket import Bucket


class UploaderTest(unittest.TestCase):
    def test_upload(self):
        request = DeliveryRequest("abcdef",
                                  "test",
                                  "FEEL FREE TO REMOVE ME. I AM A TEST.",
                                  "origin",
                                  "destination",
                                  reward=10,
                                  weight=2,
                                  fragile=True,
                                  status=Status.AVAILABLE,
                                  money_lock=0,
                                  owner='person A',
                                  assistant='person B')

        DeliveryRequestUploader.upload(request)

    def test_get_invalid_url_should_return_empty_string(self):
        something = Bucket.get_url("some_invalid_url")
        self.assertIsNone(something)
        something = Bucket.get_url(45)
        self.assertIsNone(something)
