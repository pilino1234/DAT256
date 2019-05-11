import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_uploader import DeliveryRequestUploader


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

        try:
            DeliveryRequestUploader.upload(request)
        except:
            self.fail()
