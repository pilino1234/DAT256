import unittest

from model.user_getter import UserGetter


class UserGetterTest(unittest.TestCase):
    def test_get_existing_user(self):
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')

        self.assertIsNotNone(user)
        self.assertEqual(
            user.name, "Travis CI Account - DON'T DELETE OR YOULL BREAK THE "
            "ENTIRE CI WORKFLOW/UNITTESTS REEEEEEEEEEEEEEEEEEEEEEEE")
        self.assertEqual(user.mail, "travis@carrepsa.ci")
        self.assertEqual(user.phonenumber, "0")

    def test_getting_nonexistent_user(self):
        user = UserGetter.get_by_id('non_existent_uid')
        self.assertIsNone(user)

    def test_getting_blank_user(self):
        user = UserGetter.get_by_id("")
        self.assertIsNone(user)
