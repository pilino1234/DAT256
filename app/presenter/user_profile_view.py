from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty
from kivymd.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from model.user import User

Builder.load_file("view/user_profile_view.kv")


class WhiteCardButton(MDRaisedButton):
    """Widget that alters MDRaisedButton to a blank card-looking button with a drop shadow."""

    _radius = NumericProperty(dp(14))


class MenuField(WhiteCardButton):
    """Widget that represents the content of a menu field."""

    def __init__(self, title: str, data: str, editable: bool, **kwargs):
        """Initializes the delivery list"""
        super(WhiteCardButton, self).__init__(**kwargs)
        self.ids.field_title.text = title
        self.ids.field_data.text = data
        self.editable = editable
        if not editable:
            self.remove_widget(self.ids.edit_button_container)

    def set_data(self, data: str):
        """Overwrite the data stored."""
        self.ids.field_data.text = data


class UserProfileView(RelativeLayout):
    """The main view for viewing and editing the user profile."""

    field_editing = ""  # Keep track of which field is being edited (if any)
    widget_input = ""  # Keep track of widget for getting input in order to be able to delete it.
    avatar_edit_widget = ""
    _back_button_handler = ObjectProperty(None)

    user_me = User(
        name="Jiggly Puff",
        mail="jiggly@puff.com",
        phone="0706123123",
        avatar="something image related here, not used atm",
        balance=1498)

    user_viewing = user_me

    def __init__(self, **kwargs):
        """Initializes the user profile."""
        super(RelativeLayout, self).__init__()
        if 'user' in kwargs:
            self.user_viewing = kwargs['user']
        if 'back_button_handler' in kwargs:
            self._back_button_handler = kwargs['back_button_handler']
        else:
            self.ids.scroll_view_container.remove_widget(self.ids.back_button)
        self._init_content()

    def _init_content(self):
        """Initializes the user profile."""
        self.name_field = MenuField("Name", self.user_viewing.name,
                                    self.user_viewing == self.user_me)
        self.ids.scroll_view_container.add_widget(self.name_field)

        self.phone_field = MenuField("Phone", self.user_viewing.phone,
                                     self.user_viewing == self.user_me)
        self.ids.scroll_view_container.add_widget(self.phone_field)

        self.mail_field = MenuField("Mail", self.user_viewing.mail,
                                    self.user_viewing == self.user_me)
        self.ids.scroll_view_container.add_widget(self.mail_field)

        if self.user_viewing == self.user_me:
            self.balance_field = MenuField(
                "Account Balance",
                str(self.user_viewing.balance) + " SEK", False)
            self.ids.scroll_view_container.add_widget(self.balance_field)
            self.balance_field.add_widget(AccountButtons())

        self.widget_input = AnswerInput()

    def update_fields(self):
        """Update displayed information from the user data."""
        self.name_field.set_data(self.user_viewing.name)
        self.phone_field.set_data(self.user_viewing.phone)
        self.mail_field.set_data(self.user_viewing.mail)
        self.balance_field.set_data(str(self.user_viewing.balance) + " SEK")

    def request_edit(self, field):
        """Called when any of the edit buttons are released."""
        self.field_editing = field
        if field == "Name":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.name
        if field == "Mail":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.mail
        if field == "Phone":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.phone
        if field == "deposit":
            self.widget_input.ids.title.text = "Deposit Money"
            self.widget_input.ids.text_input.text = "0"
        if field == "withdraw":
            self.widget_input.ids.title.text = "Withdraw Money"
            self.widget_input.ids.text_input.text = "0"

        self.remove_widget(self.widget_input)
        self.add_widget(self.widget_input)

    def do_edit(self, text):
        """Called when the edit button in the edit widget is released."""
        # If no input given, cancel edit (do nothing and remove popup)
        if text is None or text == "":
            self.remove_widget(self.widget_input)
            return

        if self.field_editing == "Name":
            self.user_me.name = text
        if self.field_editing == "Phone":
            self.user_me.phone = text
        if self.field_editing == "Mail":
            self.user_me.mail = text
        if self.field_editing == "avatar":
            self.user_me.avatar = text

        if self.field_editing == "deposit":
            amount = int(text)
            self.user_me.deposit(amount)

        if self.field_editing == "withdraw":
            amount = int(text)
            if amount <= self.user_me.balance:
                self.user_me.withdraw(amount)

        self.update_fields()
        self.remove_widget(self.widget_input)  # Remove the edit widget

    def logout(self):
        print("logout")


class AnswerInput(BoxLayout):
    """A widget that asks the user for input"""

    pass


class AccountButtons(RelativeLayout):
    """A widget that displays the deposit and withdraw buttons"""

    pass


class RoundImage(FloatLayout):
    """A cropped round image"""

    pass
