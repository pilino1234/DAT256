from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen

from model.firebase.auth import Auth
from model.user_me_getter import UserMeGetter

Builder.load_file("view/screens/auth_screen.kv")


class AuthScreen(Screen):
    """The screen containing all authentication related views."""

    def __init__(self, **kwargs):
        super(AuthScreen, self).__init__(**kwargs)

        credential_store = JsonStore('credentials.json')

        if credential_store.exists('tokens'):
            try:
                user_id = Auth.sign_in_with_tokens(**credential_store.get('tokens'))

                UserMeGetter.set_me(user_id)
                app = App.get_running_app()
                app.is_authenticated = True
            except Exception as error:
                print(error)
                print("Deleting credentials.json since it may be corrupted")
                # credential_store.delete('tokens')
