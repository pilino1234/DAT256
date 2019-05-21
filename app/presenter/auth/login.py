from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.firebase.auth import Auth
from model.user_me_getter import UserMeGetter

Builder.load_file("view/auth/login.kv")


class Login(BoxLayout):
    """The login view"""

    def authenticate(self):
        email = self.ids.email_tf.text
        password = self.ids.password_tf.text
        user_id = Auth.sign_in(email, password)

        if not user_id:
            print("Something went wrong")
        else:
            UserMeGetter.set_me(user_id)
            app = App.get_running_app()
            app.is_authenticated = True
