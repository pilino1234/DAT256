class MinifiedUser:
    """Represents a public version of a user's account."""

    def __init__(self, name: str, mail: str, phonenumber: str, uid: str):
        self.name = name
        self.mail = mail
        self.phonenumber = phonenumber
        self.uid = uid

    def update(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'mail' in kwargs:
            self.mail = kwargs['mail']
        if 'phonenumber' in kwargs:
            self.phonenumber = kwargs['phonenumber']
        if 'uid' in kwargs:
            self.uid = kwargs['uid']

    def __eq__(self, other):
        """Checks equality between users using their mail."""
        return isinstance(other, MinifiedUser) and self.mail == other.mail

    def __str__(self):
        """Format a user for printing"""
        return "User: {name}, {mail}, {phonenumber}".format(
            name=self.name, mail=self.mail, phonenumber=self.phonenumber)

    def to_dict(self):
        return {
            "name": self.name,
            "mail": self.mail,
            "phonenumber": self.phonenumber,
            "uid": self.uid
        }
