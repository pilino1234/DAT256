import unittest

from model.delivery_request import DeliveryRequest, Status
from model.user import User


class UserTest(unittest.TestCase):
    def test_equal(self):
        u1 = User()
        u1.update("User1",
                  "email@example.com",
                  "1234567890",
                  "",
                  balance=0,
                  packages=[])

        u2 = User()
        u2.update("User2",
                  "email@example.com",
                  "0987654321",
                  "avatar_binary_string_stuff",
                  balance=10,
                  packages=[])

        self.assertTrue(u1 == u2)
        self.assertTrue(u2 == u1)

    def test_not_equal(self):

        u1 = User()
        u1.update("User1",
                  "email@example.com",
                  "1234567890",
                  "",
                  balance=0,
                  packages=[])

        u2 = User()
        u2.update("User1",
                  "different_email@example.com",
                  "1234567890",
                  "",
                  balance=0,
                  packages=[])

        self.assertFalse(u1 == u2)
        self.assertFalse(u2 == u1)

    def test_deposit(self):
        user = User()
        user.update("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=0,
                    packages=[])

        self.assertEqual(user.balance, 0)
        user.deposit(100)
        self.assertEqual(user.balance, 100)

    def test_deposit_negative(self):
        user = User()
        user.update("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=50,
                    packages=[])

        self.assertEqual(user.balance, 50)
        user.deposit(-10)
        self.assertEqual(user.balance, 50)

    def test_withdraw(self):
        user = User()
        user.update("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    packages=[])

        self.assertEqual(user.balance, 100)
        user.withdraw(50)
        self.assertEqual(user.balance, 50)

    def test_withdraw_negative(self):
        user = User()
        user.update("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    packages=[])

        self.assertEqual(user.balance, 100)
        user.withdraw(-50)
        self.assertEqual(user.balance, 100)

    def test_withdraw_more_than_balance(self):
        user = User()
        user.update("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    packages=[])

        self.assertEqual(user.balance, 100)
        user.withdraw(1000000)
        self.assertEqual(user.balance, 100)

    def test_locking_money(self):
        user = User()
        user.update("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    packages=[])

        request = DeliveryRequest("id",
                                  "item",
                                  "description\ntext",
                                  "origin",
                                  "destination",
                                  reward=50,
                                  weight=2,
                                  fragile=True,
                                  status=Status.AVAILABLE,
                                  money_lock=0,
                                  owner="",
                                  assistant="",
                                  image_path="")

        self.assertEqual(user.balance, 100)
        user.lock_delivery_amount(request)
        self.assertEqual(user.balance, 50)
