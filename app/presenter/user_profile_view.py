from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty
from kivymd.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from model.firebase.auth import Auth
from model.user_me_getter import UserMeGetter

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

    def __init__(self, **kwargs):
        """Initializes the user profile."""
        super(RelativeLayout, self).__init__()
        if 'user' in kwargs:
            self.user_viewing = kwargs['user']
        else:
            self.user_viewing = UserMeGetter.user
        if 'back_button_handler' in kwargs:
            self._back_button_handler = kwargs['back_button_handler']
        else:
            self.ids.scroll_view_container.remove_widget(self.ids.back_button)
        self.user_viewing.on_update(self.update_fields)
        self._init_content()

    def _init_content(self):
        """Initializes the user profile."""
        user_me = UserMeGetter.user

        self.name_field = MenuField("Name", self.user_viewing.name,
                                    self.user_viewing == user_me)
        self.ids.scroll_view_container.add_widget(self.name_field)

        self.phone_field = MenuField("Phone", self.user_viewing.phonenumber,
                                     self.user_viewing == user_me)
        self.ids.scroll_view_container.add_widget(self.phone_field)

        self.mail_field = MenuField("Mail", self.user_viewing.mail,
                                    self.user_viewing == user_me)
        self.ids.scroll_view_container.add_widget(self.mail_field)

        if self.user_viewing == user_me:
            self.balance_field = MenuField(
                "Account Balance",
                str(self.user_viewing.balance) + " SEK", False)
            self.ids.scroll_view_container.add_widget(self.balance_field)
            self.balance_field.add_widget(AccountButtons())

        self.widget_input = AnswerInput()

    def update_fields(self):
        """Update displayed information from the user data."""
        self.name_field.set_data(self.user_viewing.name)
        self.phone_field.set_data(self.user_viewing.phonenumber)
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
            self.widget_input.ids.text_input.text = self.user_viewing.phonenumber
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

        user_me = UserMeGetter.user

        if self.field_editing == "Name":
            user_me.update(name=text)
        if self.field_editing == "Phone":
            user_me.update(phonenumber=text)
        if self.field_editing == "Mail":
            user_me.update(mail=text)
        if self.field_editing == "avatar":
            user_me.update(avatar=text)
        if self.field_editing == "deposit":
            amount = int(text)
            user_me.deposit(amount)
        if self.field_editing == "withdraw":
            amount = int(text)
            user_me.withdraw(amount)

        self.update_fields()
        self.remove_widget(self.widget_input)  # Remove the edit widget

    def logout(self):
        """Log out the user"""
        Auth.sign_out()
        App.get_running_app().is_authenticated = False


class AnswerInput(BoxLayout):
    """A widget that asks the user for input"""

    pass


class AccountButtons(RelativeLayout):
    """A widget that displays the deposit and withdraw buttons"""

    pass


class RoundImage(FloatLayout):
    """A cropped round image"""

    pass
