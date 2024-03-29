from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.firebase.auth import Auth

Builder.load_file("view/auth/login.kv")


class Login(BoxLayout):
    """The login view"""

    def authenticate(self):
        """Callback when the user clicks login, and uses Auth to sign in and set up credentials"""
        email = self.ids.email_tf.text
        password = self.ids.password_tf.text
        user_id = Auth.sign_in(email, password)

        if not user_id:
            print("Something went wrong")
