import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_uploader import DeliveryRequestUploader


class DictConverterTest(unittest.TestCase):
    def test_conversion(self):
        request = DeliveryRequest("item", "description\ntext",
                                  "origin", "destination",
                                  reward=10, weight=2, fragile=True,
                                  status=Status.AVAILABLE, money_lock=0)

        request_dict = DeliveryRequestUploader.request_to_dict(request)

        expected = {'description': 'description\ntext',
                    'destination': 'destination',
                    'fragile': True,
                    'item': 'item',
                    'money_lock': 0,
                    'origin': 'origin',
                    'reward': 10,
                    'status': 0,
                    'weight': 2}

        self.assertDictEqual(request_dict, expected,
                             msg="The converted dict should equal the expected dict. "
                                 "You may want to check the data definition in the team "
                                 "GDrive to confirm all data is present and correct.")
