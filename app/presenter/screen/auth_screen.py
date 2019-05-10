from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/screens/auth_screen.kv")


class AuthScreen(Screen):
    """The screen containing all authentication related views."""

    pass
