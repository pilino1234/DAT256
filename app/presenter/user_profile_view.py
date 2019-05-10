from kivy.lang import Builder

from kivy.uix.relativelayout import RelativeLayout

from model.user import User
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import NumericProperty

from kivymd.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

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

    user_me = User("Jiggly Puff",
                   "jiggly@puff.com",
                   "0706123123",
                   "something image related here, not used atm",
                   balance=1498,
                   rating=4.3)

    user_viewing = user_me

    def __init__(self, **kwargs):
        """Initializes the user profile."""
        super(RelativeLayout, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, wtf):
        """Initializes the user profile."""
        self.name_field = MenuField("Name", self.user_viewing.name,
                                    self.user_viewing == self.user_me)
        self.ids.scroll_view_container.add_widget(self.name_field)

        self.phone_field = MenuField("Phone", self.user_viewing.phone,
                                     self.user_viewing == self.user_me)
        self.ids.scroll_view_container.add_widget(self.phone_field)

        self.email_field = MenuField("E-mail", self.user_viewing.email,
                                     self.user_viewing == self.user_me)
        self.ids.scroll_view_container.add_widget(self.email_field)

        if self.user_viewing == self.user_me:
            self.balance_field = MenuField(
                "Account Balance",
                str(self.user_viewing.balance) + " SEK", False)
            self.ids.scroll_view_container.add_widget(self.balance_field)
            self.balance_field.add_widget(AccountButtons())

        self.rating_field = MenuField("Rating",
                                      str(self.user_viewing.rating) + " / 5",
                                      False)
        self.ids.scroll_view_container.add_widget(self.rating_field)

        self.widget_input = AnswerInput()

    def update_fields(self):
        """Update displayed information from the user data."""
        self.name_field.set_data(self.user_viewing.name)
        self.phone_field.set_data(self.user_viewing.phone)
        self.email_field.set_data(self.user_viewing.email)
        self.balance_field.set_data(str(self.user_viewing.balance) + " SEK")
        self.rating_field.set_data(str(self.user_viewing.rating) + " / 5")

    def request_edit(self, field):
        """Called when any of the edit buttons are released."""
        self.field_editing = field
        if field == "Name":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.name
        if field == "E-mail":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.email
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

        if self.field_editing == "Name":
            self.user_me.name = text
        if self.field_editing == "Phone":
            self.user_me.phone = text
        if self.field_editing == "E-mail":
            self.user_me.email = text
        if self.field_editing == "avatar":
            self.user_me.avatar = text

        if self.field_editing == "deposit":
            amount = int(text)
            self.user_me.balance = self.user_me.balance + amount

        if self.field_editing == "withdraw":
            amount = int(text)
            if amount <= self.user_me.balance:
                self.user_me.balance = self.user_me.balance - amount

        self.update_fields()
        self.remove_widget(self.widget_input)  # Remove the edit widget

    def do_avatar_edit(self):
        """Called when editing the avatar."""
        print("Open image picker.")


class AnswerInput(BoxLayout):
    """A widget that asks the user for input"""

    pass


class AccountButtons(RelativeLayout):
    """A widget that displays the deposit and withdraw buttons"""

    pass


class RoundImage(FloatLayout):
    """A cropped round image"""

    pass
