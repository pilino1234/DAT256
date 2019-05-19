from kivy.storage.jsonstore import JsonStore

from model.firebase.auth import Auth

credential_store = JsonStore('credentials.json')

if credential_store.exists('tokens'):
    try:
        Auth.sign_in_with_tokens(**credential_store.get('tokens'))
    except Exception as error:
        print(error)
        print("Deleting credentials.json since it may be corrupted")
        credential_store.delete('tokens')
