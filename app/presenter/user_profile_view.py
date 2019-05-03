from kivy.lang import Builder

from kivy.uix.relativelayout import RelativeLayout

from model.user import User
from kivy.clock import Clock

from kivymd.button import MDFloatingActionButton
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file("view/user_profile_view.kv")


class EditButton(MDFloatingActionButton):

    def __init__(self, field_editing, **kwargs):
        super(MDFloatingActionButton, self).__init__(**kwargs)
        self.field_editing = field_editing


class UserProfileView(RelativeLayout):

    user_me = User(
        "Name Surname",
        "asdf@example.com",
        "0706123123",
        "https://vignette.wikia.nocookie.net/jamesbond/images/8/81/James_Bond_%28Daniel_Craig%29_-_Profile.jpg/revision/latest?cb=20150405210952"
    )
    user_viewing = User(
        "Name Surname",
        "asdf@example.com",
        "0706123123",
        "https://vignette.wikia.nocookie.net/jamesbond/images/8/81/James_Bond_%28Daniel_Craig%29_-_Profile.jpg/revision/latest?cb=20150405210952"
    )

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, wtf):

        if self.user_viewing.equals(self.user_me):
            self.ids.user_name_box.add_widget(EditButton("name"))
            self.ids.user_phone_box.add_widget(EditButton("phone"))
            self.ids.user_email_box.add_widget(EditButton("email"))

    def edit_button_callback(self, name):
        print(name)

