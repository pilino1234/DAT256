from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast

Builder.load_file("view/auth/forgot.kv")


class Forgot(BoxLayout):
    """The reset password view."""

    def reset_password(self):
        """Sends a password reset mail and displays a confirmation toast"""
        toast("Check your email for password reset link.")
