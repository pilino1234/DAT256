class User:

    def __init__(self, name, email, phone, avatar, account_balance, rating):
        self.name = name
        self.email = email
        self.phone = phone
        self.avatar = avatar
        self.account_balance = account_balance
        self.rating = rating

    def replace_all(self, name, email, phone, avatar, account_balance, rating):
        self.replace_all(name, email, phone, avatar)

        self.account_balance = account_balance
        self.rating = rating

    def replace_all(self, name, email, phone, avatar):
        self.name = name
        self.email = email
        self.phone = phone
        self.avatar = avatar

    def set_rating(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.rating

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def get_account_balance(self):
        return self.account_balance

    def equals(self, user):
        return self.email == user.email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_avatar(self):
        return self.avatar

    def set_avatar(self, avatar):
        self.avatar = avatar



