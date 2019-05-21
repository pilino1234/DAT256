from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.firebase.auth import Auth

Builder.load_file("view/auth/register.kv")


class Register(BoxLayout):
    """The registration view"""

    def register(self):
        email = self.ids.email_tf.text
        password = self.ids.password_tf.text
        password_repeat = self.ids.password_repeat_tf.text
        name = self.ids.name_tf.text
        phonenumber = self.ids.phonenumber_tf.text

        if password == password_repeat:
            Auth.sign_up(email, password, name, phonenumber)
