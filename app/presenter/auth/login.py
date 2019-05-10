from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("view/auth/login.kv")


class Login(BoxLayout):
    """The login view"""

    def authenticate(self):
        app = App.get_running_app()
        app.is_authenticated = True
