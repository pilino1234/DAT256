from kivy.lang import Builder

from kivy.uix.relativelayout import RelativeLayout

from model.user import User
from kivy.clock import Clock
from kivymd.cards import MDCard
from kivymd.textfields import MDTextField

from kivymd.button import MDFloatingActionButton
from kivy.uix.boxlayout import BoxLayout


Builder.load_file("view/user_profile_view.kv")


class EditButton(MDFloatingActionButton):

    def __init__(self, field_editing, **kwargs):
        super(MDFloatingActionButton, self).__init__(**kwargs)
        self.field_editing = field_editing


class AnswerInput(BoxLayout):
    pass


class UserProfileView(RelativeLayout):

    field_editing = ""  # Keep track of which field is being edited (if any)
    widget_input = ""  # Keep track of widget for getting input in order to be able to delete it.

    user_me = User(
        "Name Surname",
        "asdf@example.com",
        "0706123123",
        "https://vignette.wikia.nocookie.net/jamesbond/images/8/81/James_Bond_%28Daniel_Craig%29_-_Profile.jpg/revision/latest?cb=20150405210952"
    )

    '''
    user_viewing = User(
        "Name Surname2",
        "asdf@example.com",
        "0706123123",
        "https://vignette.wikia.nocookie.net/jamesbond/images/8/81/James_Bond_%28Daniel_Craig%29_-_Profile.jpg/revision/latest?cb=20150405210952"
    )
    '''
    user_viewing = user_me

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, wtf):  # If viewing my own profile, add edit buttons
        if self.user_viewing.equals(self.user_me):
            self.ids.user_name_box.add_widget(EditButton("name"))
            self.ids.user_phone_box.add_widget(EditButton("phone"))
            self.ids.user_email_box.add_widget(EditButton("email"))
            self.ids.user_avatar_box.add_widget(EditButton("avatar"))

    def edit_button_callback(self, field):  # Called when any of the edit buttons are released
        self.field_editing = field  # Which edit button whas pressed. name, email or phone.
        self.widget_input = AnswerInput()
        self.add_widget(self.widget_input)

    def update_fields(self):
        self.ids.user_name_label.text = self.user_viewing.get_name()
        self.ids.user_phone_label.text = self.user_viewing.get_phone()
        self.ids.user_email_label.text = self.user_viewing.get_email()
        self.ids.user_avatar_image.source = self.user_viewing.get_avatar()

    def do_edit(self, text):  # Called when the edit button in the edit widget is released.

        if text is None or text == "":  # If no input given, cancel edit (do nothing and remove popup)
            self.remove_widget(self.widget_input)

        if self.field_editing == "name":
            self.user_me.set_name(text)
        if self.field_editing == "phone":
            self.user_me.set_phone(text)
        if self.field_editing == "email":
            self.user_me.set_email(text)
        if self.field_editing == "avatar":
            self.user_me.set_avatar(text)


        self.update_fields()
        self.remove_widget(self.widget_input)  # Remove the edit widget
