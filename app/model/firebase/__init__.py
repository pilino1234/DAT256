from kivy.storage.jsonstore import JsonStore

from model.firebase.firebase import Firebase

credential_store = JsonStore('credentials.json')

if credential_store.exists('tokens'):
    Firebase.sign_in_with_tokens(**credential_store.get('tokens'))
