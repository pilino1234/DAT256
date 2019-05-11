import unittest

from model.delivery_request import DeliveryRequest, Status


class DeliveryRequestTest(unittest.TestCase):
    def test_conversion(self):
        request = DeliveryRequest("abcdef",
                                  "item",
                                  "description\ntext",
                                  "origin",
                                  "destination",
                                  reward=10,
                                  weight=2,
                                  fragile=True,
                                  status=Status.AVAILABLE,
                                  money_lock=0,
                                  owner='person A',
                                  assistant='person B')

        request_dict = request.to_dict()

        expected = {
            'uid': 'abcdef',
            'item': 'item',
            'description': 'description\ntext',
            'origin': 'origin',
            'destination': 'destination',
            'reward': 10,
            'weight': 2,
            'fragile': True,
            'status': 0,
            'money_lock': 0,
            'owner': 'person A',
            'assistant': 'person B'
        }

        self.assertDictEqual(
            request_dict,
            expected,
            msg="The converted dict should equal the expected dict. "
            "You may want to check the data definition in the team "
            "GDrive to confirm all data is present and correct.")
