class User:
    """Represents a user's account."""

    def __init__(self, name: str, email: str, phone: str, avatar: str,
                 balance: int, rating: float):
        """Initializes the user."""
        self.name = name
        self.email = email
        self.phone = phone
        self.avatar = avatar
        self.balance = balance
        self.rating = rating

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

    def __eq__(self, other):
        """Checks equality between users using their mail."""
        return self.email == other.email
