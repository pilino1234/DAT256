import unittest

from model.delivery_request import DeliveryRequest, Status
from model.user import User


class UserTest(unittest.TestCase):
    def test_equal(self):
        u1 = User("User1",
                  "email@example.com",
                  "1234567890",
                  "",
                  balance=0,
                  rating=3)

        u2 = User("User2",
                  "email@example.com",
                  "0987654321",
                  "avatar_binary_string_stuff",
                  balance=10,
                  rating=5)

        self.assertTrue(u1 == u2)
        self.assertTrue(u2 == u1)

    def test_not_equal(self):
        u1 = User("User1",
                  "email@example.com",
                  "1234567890",
                  "",
                  balance=0,
                  rating=3)

        u2 = User("User1",
                  "different_email@example.com",
                  "1234567890",
                  "",
                  balance=0,
                  rating=3)

        self.assertFalse(u1 == u2)
        self.assertFalse(u2 == u1)

    def test_deposit(self):
        user = User("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=0,
                    rating=3)

        self.assertEqual(user.balance, 0)
        user.deposit(100)
        self.assertEqual(user.balance, 100)

    def test_deposit_negative(self):
        user = User("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=50,
                    rating=3)

        self.assertEqual(user.balance, 50)
        user.deposit(-10)
        self.assertEqual(user.balance, 50)

    def test_withdraw(self):
        user = User("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    rating=3)

        self.assertEqual(user.balance, 100)
        user.withdraw(50)
        self.assertEqual(user.balance, 50)

    def test_withdraw_negative(self):
        user = User("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    rating=3)

        self.assertEqual(user.balance, 100)
        user.withdraw(-50)
        self.assertEqual(user.balance, 100)

    def test_withdraw_more_than_balance(self):
        user = User("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    rating=3)

        self.assertEqual(user.balance, 100)
        user.withdraw(1000000)
        self.assertEqual(user.balance, 100)

    def test_locking_money(self):
        user = User("User1",
                    "email@example.com",
                    "1234567890",
                    "",
                    balance=100,
                    rating=3)

        request = DeliveryRequest("item",
                                  "description\ntext",
                                  "origin",
                                  "destination",
                                  reward=50,
                                  weight=2,
                                  fragile=True,
                                  status=Status.AVAILABLE,
                                  money_lock=0)

        self.assertEqual(user.balance, 100)
        user.lock_delivery_amount(request)
        self.assertEqual(user.balance, 50)
