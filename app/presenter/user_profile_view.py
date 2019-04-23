from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from model.user import User

Builder.load_file("view/user_profile_view.kv")


class UserProfileView(BoxLayout):
    user_me = User(
        "Name Surname",
        "asdf@example.com",
        "0706123123",
        "https://i.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg"
    )
