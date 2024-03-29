from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen

from model.firebase.auth import Auth

Builder.load_file("view/screens/auth_screen.kv")


class AuthScreen(Screen):
    """The screen containing all authentication related views."""

    def __init__(self, **kwargs):
        """Initializes auth screen, checks if there's a credentials.json and if so, signs in"""
        super(AuthScreen, self).__init__(**kwargs)

        credential_store = JsonStore('credentials.json')

        if credential_store.exists('tokens'):
            try:
                Auth.sign_in_with_tokens(**credential_store.get('tokens'))
            except Exception as error:
                print(error)
                print("Deleting credentials.json since it may be corrupted")
                credential_store.delete('tokens')
