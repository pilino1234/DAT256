from kivy.lang import Builder

from kivy.uix.relativelayout import RelativeLayout

from model.user import User
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import NumericProperty


from kivymd.cards import MDCard
from kivymd.textfields import MDTextField
from kivymd.button import MDFloatingActionButton, MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage


Builder.load_file("view/user_profile_view.kv")


class WhiteCardButton(MDRaisedButton):
    """Widget that alters MDRaisedButton to a blank card-looking button with a drop shadow."""

    _radius = NumericProperty(dp(14))


class MenuField(WhiteCardButton):
    """Widget that represents the content of a menu field."""

    editable = False  # Whether this field is editable

    def __init__(self, title, data, editable, **kwargs):
        """Initializes the delivery list"""
        super(WhiteCardButton, self).__init__(**kwargs)
        self.ids.field_title.text = title
        self.ids.field_data.text = data
        self.editable = editable
        if not editable:
            self.remove_widget(self.ids.edit_button_container)

    def set(self, title, data):
        self.ids.field_title.text = title
        self.ids.field_data.text = data


class AnswerInput(BoxLayout):
    """A widget that asks the user for input"""
    pass


class AvatarEditPrompt(BoxLayout):
    """A widget that displays different ways of changing your avatar"""
    pass


class AccountButtons(RelativeLayout):
    """A widget that displays the deposit and withdraw buttons"""
    pass


class RoundImage(FloatLayout):
    """A cropped round image"""
    pass


class UserProfileView(RelativeLayout):
    """The main view for viewing and editing the user profile."""
    field_editing = ""  # Keep track of which field is being edited (if any)
    widget_input = ""  # Keep track of widget for getting input in order to be able to delete it.
    avatar_edit_widget = ""

    user_me = User(
        "Jiggly Puff",
        "jiggly@puff.com",
        "0706123123",
        "something image related here, not used atm",
        1498,
        4.3
    )

    '''
    user_viewing = User(
        "Jiggly Puff",
        "totally_definitely_absolutely_jigglypuff@gmail.com",
        "0706123123",
        "something image related here, not used atm",
        1498,
        4.3
    )
    '''
    user_viewing = user_me

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, wtf):  # If viewing my own profile, add edit buttons
        self.name_field = MenuField("Name", self.user_viewing.get_name(), self.user_viewing.equals(self.user_me) and True)
        self.ids.scroll_view_container.add_widget(self.name_field)
        self.phone_field = MenuField("Phone", self.user_viewing.get_phone(), self.user_viewing.equals(self.user_me) and True)
        self.ids.scroll_view_container.add_widget(self.phone_field)
        self.email_field = MenuField("E-mail", self.user_viewing.get_email(), self.user_viewing.equals(self.user_me) and True)
        self.ids.scroll_view_container.add_widget(self.email_field)

        self.widget_input = AnswerInput()

        if self.user_viewing.equals(self.user_me):
            self.account_balance_field = MenuField(
                "Account Balance",
                str(self.user_viewing.get_account_balance()) + " SEK",
                self.user_viewing.equals(self.user_me) and False
            )
            self.ids.scroll_view_container.add_widget(self.account_balance_field)
            self.account_balance_field.add_widget(AccountButtons())

        self.rating_field = MenuField(
            "Rating", str(self.user_viewing.get_rating()) + "/5",
            self.user_viewing.equals(self.user_me) and False
        )
        self.ids.scroll_view_container.add_widget(self.rating_field)

    def update_fields(self):
        self.name_field.ids.field_data.text = self.user_viewing.get_name()
        self.phone_field.ids.field_data.text = self.user_viewing.get_phone()
        self.email_field.ids.field_data.text = self.user_viewing.get_email()
        self.account_balance_field.ids.field_data.text = str(self.user_viewing.get_account_balance()) + " SEK"
        self.rating_field.ids.field_data.text = str(self.user_viewing.get_rating()) + "/5"

    def request_edit(self, field):  # Called when any of the edit buttons are released
        self.field_editing = field  # Which edit button was pressed. name, email or phone.
        if field=="Name":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.get_name()
        if field=="E-mail":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.get_email()
        if field=="Phone":
            self.widget_input.ids.title.text = field
            self.widget_input.ids.text_input.text = self.user_viewing.get_phone()
        if field=="deposit":
            self.widget_input.ids.title.text = "Deposit Money"
            self.widget_input.ids.text_input.text = "0"
        if field=="withdraw":
            self.widget_input.ids.title.text = "Withdraw Money"
            self.widget_input.ids.text_input.text = "0"


        self.add_widget(self.widget_input)

    def do_edit(self, text):  # Called when the edit button in the edit widget is released.

        if text is None or text == "":  # If no input given, cancel edit (do nothing and remove popup)
            self.remove_widget(self.widget_input)

        if self.field_editing == "Name":
            self.user_me.set_name(text)
        if self.field_editing == "Phone":
            self.user_me.set_phone(text)
        if self.field_editing == "E-mail":
            self.user_me.set_email(text)
        if self.field_editing == "avatar":
            self.user_me.set_avatar(text)
        if self.field_editing == "deposit":
            self.user_me.set_account_balance(self.user_me.get_account_balance()+int(text))
        if self.field_editing == "withdraw" and int(text) <= self.user_me.get_account_balance():
            self.user_me.set_account_balance(self.user_me.get_account_balance()-int(text))

        self.update_fields()
        self.remove_widget(self.widget_input)  # Remove the edit widget

    def request_avatar_edit(self):  # Called when any of the edit buttons are released
        self.avatar_edit_widget = AvatarEditPrompt()
        self.add_widget(self.avatar_edit_widget)

    def do_avatar_edit(self, type):
        self.remove_widget(self.avatar_edit_widget)