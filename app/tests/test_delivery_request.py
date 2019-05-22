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
            'origin': {
                'name': 'Odenvägen 1, SE-194 63 Odenslunda, Sweden',
                'longitude': 59.51224,
                'latitude': 17.93536
            },
            'destination': {
                'name': 'Rolsmo 1, SE-360 24 Linneryd, Sweden',
                'longitude': 56.64989,
                'latitude': 15.16624
            },
            'reward': 10,
            'weight': 2,
            'fragile': True,
            'status': 0,
            'money_lock': 0,
            'owner': {
                'name': '',
                'mail': '',
                'phonenumber': '',
                'uid': '94MTAsYEcpTBGW98MQbjyuGEPUx1'
            },
            'assistant': {
                'name': '',
                'mail': '',
                'phonenumber': '',
                'uid': ''
            },
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
            "Delivery request TEST | item, from: Location: (59.51224, 17.93536) Odenvägen 1, SE-194 63 Ode"
            +
            "nslunda, Sweden -> to: Location: (56.64989, 15.16624) Rolsmo 1, SE-360 24 Linneryd, Sweden, rew"
            +
            "ard: 10, money_lock: 0, weight: 2, fragile: True, status: 0, description: This a test, feel fre"
            + "e to remove., image_path: ")

    def test_distance_pretty(self):
        request = create_delivery_request()
        self.assertEqual(request.distance_pretty, "432.7 km")

    def test_reward_pretty(self):
        request = create_delivery_request()
        self.assertEqual(request.reward_pretty, "10 kr")
