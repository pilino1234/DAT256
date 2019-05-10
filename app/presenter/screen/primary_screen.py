from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/screens/primary_screen.kv")


class PrimaryScreen(Screen):
    """
    The primary screen of the app.

    Contains everything except authentication.
    """

    def logout(self):
        """Log out the user"""
        app = App.get_running_app()
        app.is_authenticated = False
