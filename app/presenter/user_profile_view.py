from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from model.user import User

from kivymd.button import MDFloatingActionButton


Builder.load_file("view/user_profile_view.kv")


class UserProfileView(BoxLayout):
    user_me = User(
        "Name Surname",
        "asdf@example.com",
        "0706123123",
        "https://vignette.wikia.nocookie.net/jamesbond/images/8/81/James_Bond_%28Daniel_Craig%29_-_Profile.jpg/revision/latest?cb=20150405210952"
    )
