from kivy.storage.jsonstore import JsonStore

from model.firebase.auth import Auth

credential_store = JsonStore('credentials.json')

if credential_store.exists('tokens'):
    Auth.sign_in_with_tokens(**credential_store.get('tokens'))
