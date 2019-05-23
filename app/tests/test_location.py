import unittest

from model.location import Location


class LocationTest(unittest.TestCase):
    def test_to_dict(self):
        location1 = Location('test', 0.0, 0.0)

        expected = {
            'name': 'test',
            'latitude': 0,
            'longitude': 0
        }

        self.assertDictEqual(location1.to_dict(), expected)

    def test_from_dict(self):
        data = {
            'name': 'test',
            'latitude': 0,
            'longitude': 0
        }

        location = Location.from_dict(data)

        self.assertEqual(location.name, data['name'])
        self.assertEqual(location.latitude, data['latitude'])
        self.assertEqual(location.longitude, data['longitude'])

    def test_dist_to(self):
        location1 = Location('test', 0.0, 0.0)
        location2 = Location('test', 10.0, 10.0)

        self.assertEqual(location1.dist_to(location2), 1565.1090992178997)
        self.assertEqual(location2.dist_to(location1), 1565.1090992178997)

    def test_is_close_to(self):
        location1 = Location('test', 0.0, 0.0)
        location2 = Location('test', 0.02, 0.02)
        location3 = Location('test', 0.04, 0.01)

        self.assertTrue(location1.is_close_to(location2))
        self.assertTrue(location2.is_close_to(location1))

        self.assertTrue(location1.is_close_to(location3))
        self.assertTrue(location3.is_close_to(location1))

        self.assertTrue(location2.is_close_to(location3))
        self.assertTrue(location3.is_close_to(location2))

    def test_is_not_close_to(self):
        location1 = Location('test', 0.0, 0.0)
        location2 = Location('test', 10.0, 10.0)
        location3 = Location('test', -0.04, -1.0)

        self.assertFalse(location1.is_close_to(location2))
        self.assertFalse(location2.is_close_to(location1))

        self.assertFalse(location1.is_close_to(location3))
        self.assertFalse(location3.is_close_to(location1))

        self.assertFalse(location2.is_close_to(location3))
        self.assertFalse(location3.is_close_to(location2))

    def test_to_string(self):
        location = Location('test', 1.0, -5.0)

        expected = 'Location: (1.0, -5.0) test'

        self.assertEqual(str(location), expected)
