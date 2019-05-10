from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.firebase import Firebase

Builder.load_file("view/auth/login.kv")


class Login(BoxLayout):
    """The login view"""

    def authenticate(self):
        email = self.ids.email_tf.text
        password = self.ids.password_tf.text
        if(Firebase.sign_in(email, password)):
            app = App.get_running_app()
            app.is_authenticated = True
        else:
            print("Something went wrong")