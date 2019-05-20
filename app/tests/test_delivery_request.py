import unittest

from tests.utils import create_delivery_request


class DeliveryRequestTest(unittest.TestCase):
    def test_conversion(self):
        request = create_delivery_request()

        request_dict = request.to_dict()

        expected = {
            'uid': 'TEST',
            'item': 'item',
            'description': 'This a test, feel free to remove.',
            'origin': 'origin',
            'destination': 'destination',
            'reward': 10,
            'weight': 2,
            'fragile': True,
            'status': 0,
            'money_lock': 0,
            'owner': 'TRAVIS_TEST',
            'assistant': 'person B',
            'image_path': ''
        }

        self.assertDictEqual(
            request_dict,
            expected,
            msg="The converted dict should equal the expected dict. "
            "You may want to check the data definition in the team "
            "GDrive to confirm all data is present and correct.")

    def test_to_string(self):
        request = create_delivery_request()
        self.assertEqual(
            str(request),
            "Delivery request TEST | item, from: origin -> to: destination," +
            " reward: 10, money_lock: 0, weight: 2, fragile: True, status: 0,"
            + " description: This a test, feel free to remove., image_path: ")

    def test_distance_pretty(self):
        request = create_delivery_request()
        self.assertEqual(request.distance_pretty, "7 km")

    def test_reward_pretty(self):
        request = create_delivery_request()
        self.assertEqual(request.reward_pretty, "10 kr")
