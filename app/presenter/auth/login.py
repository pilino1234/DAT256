from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.firebase.auth import Auth

Builder.load_file("view/auth/login.kv")


class Login(BoxLayout):
    """The login view"""

    def authenticate(self):
        email = self.ids.email_tf.text
        password = self.ids.password_tf.text
        result = Auth.sign_in(email, password)

        if not result:
            print("Something went wrong")