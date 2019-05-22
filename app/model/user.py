from typing import List

from model.delivery_request import DeliveryRequest
from model.firebase.firestore import Firestore
from model.minified_user import MinifiedUser


class User:
    """Represents a user's account."""

    def __init__(self, _uid: str, name: str, mail: str, phonenumber: str,
                 avatar: str, balance: int):
        """
        Initializes a user model with the given parameters

        :param _uid: The user id
        :param name: The name of the user
        :param mail: The mail of the user
        :param phonenumber: The phonenumber of the user
        :param avatar: The link to the firebase storage image of the user
        :param balance: The current balance of the user
        """
        self._uid = _uid
        self.name = name
        self.mail = mail
        self.phonenumber = phonenumber
        self.avatar = avatar
        self.balance = balance
        self.packages: List[DeliveryRequest] = []
        self.deliveries: List[DeliveryRequest] = []

    def update(self, **kwargs):
        """
        Updates the specified props to the user model and firebase

        :param kwargs: Can be name, mail, phonenumber etc
        """
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'mail' in kwargs:
            self.mail = kwargs['mail']
        if 'phonenumber' in kwargs:
            self.phonenumber = kwargs['phonenumber']
        if 'avatar' in kwargs:
            self.avatar = kwargs['avatar']
        if 'balance' in kwargs:
            self.balance = kwargs['balance']
        if 'packages' in kwargs:
            self.packages: List[DeliveryRequest] = kwargs['packages']
        if 'deliveries' in kwargs:
            self.deliveries: List[DeliveryRequest] = kwargs['deliveries']

        with Firestore.batch('users') as batch:
            batch.set(
                self._uid, {
                    "mail": self.mail,
                    "name": self.name,
                    "phonenumber": self.phonenumber,
                    "avatar": self.avatar,
                    "balance": self.balance
                })

    def deposit(self, amount: int):
        """
        Deposit money to the users account balance.

        The amount must be greater than 0.

        :param amount: The amount to deposit
        :type amount: int
        """
        if amount > 0:
            self.balance += amount
            self.update()

    def withdraw(self, amount: int):
        """
        Withdraw money from the users account balance.

        The amount must the greater than 0, and less than the users
        current balance.

        :param amount: The amount to withdraw
        :type amount: int
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.update()

    def lock_delivery_amount(self, delivery: DeliveryRequest):
        """
        Reserves the payment amount required to pay for a delivery.

        :param delivery: The delivery request for which the payment amount should be locked.
        :type delivery: DeliveryRequest
        """
        self.balance -= delivery.reward
        self.update()

    def __eq__(self, other):
        """Checks equality between users using their mail."""
        return isinstance(other, User) and self.mail == other.mail

    def __str__(self):
        """Format a user for printing"""
        return "User: {name}, {mail}, {phonenumber}, Avatar: " \
               "{avatar}, Balance: {balance}"\
            .format(name=self.name,
                    mail=self.mail,
                    phonenumber=self.phonenumber,
                    avatar=self.avatar,
                    balance=self.balance)

    def to_minified(self):
        """Returns the user as a MinifiedUser"""
        return MinifiedUser(name=self.name,
                            phonenumber=self.phonenumber,
                            mail=self.mail,
                            uid=self._uid)
