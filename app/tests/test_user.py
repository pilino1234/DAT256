import unittest

from model.delivery_request import DeliveryRequest, Status
from model.user import User
from model.location import Location
from model.minified_user import MinifiedUser
from model.user_getter import UserGetter


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
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')

        user_balance = user.balance
        user.deposit(100)
        self.assertEqual(user.balance, user_balance + 100)

    def test_deposit_negative(self):
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')

        user_balance = user.balance
        user.deposit(-100)
        # Money should not be deposited
        self.assertEqual(user.balance, user_balance)

    def test_withdraw(self):
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')
        user.deposit(100)  # Ensure that we have enough money to withdraw
        user_balance = user.balance
        user.withdraw(50)
        self.assertEqual(user.balance, user_balance - 50)

    def test_withdraw_negative(self):
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')
        user_balance = user.balance
        user.withdraw(-100)
        # Money should not be withdrawn
        self.assertEqual(user.balance, user_balance)

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
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')

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
            owner=user.to_minified().to_dict(),
            assistant=MinifiedUser("", "", "", "").to_dict(),
            image_path="")

        # ensure enough capital
        user.deposit(100)
        user_balance = user.balance
        self.assertEqual(user.balance, user_balance)
        user.lock_delivery_amount(request)
        self.assertEqual(user.balance, user_balance - 50)
