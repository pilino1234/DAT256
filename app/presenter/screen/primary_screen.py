from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/screens/primary_screen.kv")


class PrimaryScreen(Screen):
    """
    The primary screen of the app.

    Contains everything except authentication.
    """

