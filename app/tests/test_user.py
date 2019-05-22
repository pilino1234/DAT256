import unittest

from model.delivery_request import DeliveryRequest, Status
from model.user import User
from model.location import Location
from model.minified_user import MinifiedUser


class UserTest(unittest.TestCase):
    def test_equal(self):
        u1 = User("",
                  "User1",
                  "email@example.com",
                  "1234567890",
                  "",
                  balance=0)

        u2 = User("",
                  "User2",
                  "email@example.com",
                  "0987654321",
                  "avatar_binary_string_stuff",
                  balance=10)

        self.assertTrue(u1 == u2)
        self.assertTrue(u2 == u1)

    def test_not_equal(self):

        u1 = User("",
                  "User1",
                  "email@example.com",
                  "1234567890",
                  "",
                  balance=0)

        u2 = User("",
                  "User1",
                  "different_email@example.com",
                  "1234567890",
                  "",
                  balance=0)

        self.assertFalse(u1 == u2)
        self.assertFalse(u2 == u1)

    def test_deposit(self):
        user = User("",
                    "User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=0)

        self.assertEqual(user.balance, 0)
        user.deposit(100)
        self.assertEqual(user.balance, 100)

    def test_deposit_negative(self):
        user = User("",
                    "User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=50)

        self.assertEqual(user.balance, 50)
        user.deposit(-10)
        self.assertEqual(user.balance, 50)

    def test_withdraw(self):
        user = User("",
                    "User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100)

        self.assertEqual(user.balance, 100)
        user.withdraw(50)
        self.assertEqual(user.balance, 50)

    def test_withdraw_negative(self):
        user = User("",
                    "User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100)

        self.assertEqual(user.balance, 100)
        user.withdraw(-50)
        self.assertEqual(user.balance, 100)

    def test_withdraw_more_than_balance(self):
        user = User("",
                    "User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100)

        self.assertEqual(user.balance, 100)
        user.withdraw(1000000)
        self.assertEqual(user.balance, 100)

    def test_locking_money(self):
        user = User("",
                    "User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100)

        request = DeliveryRequest(
            "id",
            "item",
            "description\ntext",
            origin=Location("Odenvägen 1, SE-194 63 Odenslunda, Sweden",
                            59.51224, 17.93536).to_dict(),
            destination=Location("Rolsmo 1, SE-360 24 Linneryd, Sweden",
                                 56.64989, 15.16624).to_dict(),
            reward=50,
            weight=2,
            fragile=True,
            status=Status.AVAILABLE,
            money_lock=0,
            owner=MinifiedUser("", "", "",
                               "94MTAsYEcpTBGW98MQbjyuGEPUx1").to_dict(),
            assistant=MinifiedUser("", "", "", "").to_dict(),
            image_path="")

        self.assertEqual(user.balance, 100)
        user.lock_delivery_amount(request)
        self.assertEqual(user.balance, 50)
