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

    def __eq__(self, other):
        """Checks equality between users using their mail."""
        return self.email == other.email
