from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty
from kivymd.cards import MDCard

from model.minified_user import MinifiedUser

Builder.load_file("view/minified_user_profile_view.kv")


class Field(MDCard):
    """Widget that alters MDRaisedButton to a blank card-looking button with a drop shadow."""

    def __init__(self, title: str, data: str, **kwargs):
        """Initializes Field with title and data"""
        super().__init__(**kwargs)
        self.ids.field_title.text = title
        self.ids.field_data.text = data

    def set_data(self, data: str):
        """Updates the data in Field"""
        self.ids.field_data.text = data

    _radius = NumericProperty(dp(14))


class MinifiedUserProfileView(RelativeLayout):
    """The main view for viewing and editing the user profile."""

    _back_button_handler = ObjectProperty(None)

    def __init__(self, user: MinifiedUser, back_button_handler):
        """Initializes the user profile."""
        super(RelativeLayout, self).__init__()
        self.user_viewing = user
        self._back_button_handler = back_button_handler
        self._init_content()

    def _init_content(self):
        """Initializes the user profile."""
        self.name_field = Field("Name", self.user_viewing.name)
        self.ids.scroll_view_container.add_widget(self.name_field)

        self.phone_field = Field("Phone", self.user_viewing.phonenumber)
        self.ids.scroll_view_container.add_widget(self.phone_field)

        self.mail_field = Field("Mail", self.user_viewing.mail)
        self.ids.scroll_view_container.add_widget(self.mail_field)

    def update_fields(self):
        """Update displayed information from the user data."""
        self.name_field.set_data(self.user_viewing.name)
        self.phone_field.set_data(self.user_viewing.phonenumber)
        self.mail_field.set_data(self.user_viewing.mail)
