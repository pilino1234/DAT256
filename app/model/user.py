from typing import List

from model.delivery_request import DeliveryRequest


class User:
    """Represents a user's account."""

    def __init__(self, name: str, mail: str, phone: str, avatar: str,
                 balance: int, rating: float, **kwargs):
        """Initializes the user using kwargs."""
        self.name = name
        self.mail = mail
        self.phone = phone
        self.avatar = avatar
        self.balance = balance
        self.rating = rating

        self._delivery_reservations: List[DeliveryRequest] = []

    def deposit(self, amount: int):
        """
        Deposit money to the users account balance.

        The amount must be greater than 0.

        :param amount: The amount to deposit
        :type amount: int
        """
        if amount > 0:
            self.balance += amount

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

    def lock_delivery_amount(self, delivery: DeliveryRequest):
        """
        Reserves the payment amount required to pay for a delivery.

        :param delivery: The delivery request for which the payment amount should be locked.
        :type delivery: DeliveryRequest
        """
        self._delivery_reservations.append(delivery)
        self.balance -= delivery.reward

    def __eq__(self, other):
        """Checks equality between users using their mail."""
        return self.mail == other.mail
