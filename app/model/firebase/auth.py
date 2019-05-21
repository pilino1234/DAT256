from model.firebase.firebase import Firebase
from model.firebase.firebase_credentials import FirebaseCredentials
from model.firebase.firestore import Firestore
from kivy.storage.jsonstore import JsonStore
import requests
import json

from model.user_me_getter import UserMeGetter

credential_store = JsonStore('credentials.json')

webApiKey = "AIzaSyAZyHcBO03Pf9RK0eM3ifYErGG8eP57aTA"  # Web Api Key


class Auth:
    """
    Manages authentication and account creation with Firebase
    """

    @staticmethod
    def sign_in_with_tokens(id_token, refresh_token, user_id):
        """
        Creates database and bucket for Firebase. Also updates credential store with the given tokens

        :param id_token: The JWT token from Firebase
        :param refresh_token: A refresh_token from Firebase used to renew tokens
        :param user_id: The user id for the signed in user
        :return The user id for the signed in user
        """
        credentials = FirebaseCredentials(token=id_token,
                                          refresh_token=refresh_token)
        Firebase.create_db(credentials=credentials)
        Firebase.create_bucket()

        credential_store.put('tokens',
                             id_token=id_token,
                             refresh_token=refresh_token,
                             user_id=user_id)

        return user_id

    @staticmethod
    def sign_in(mail, password):
        """
        Authenticate the user to firebase using mail and password
        :param mail: An valid mail
        :param password: A valid password with at least 8 in length
        :return: The user id for the signed in user
        """
        sign_in_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + webApiKey
        sign_in_payload = {
            "email": mail,
            "password": password,
            "returnSecureToken": True
        }
        sign_in_request = requests.post(sign_in_url, data=sign_in_payload)

        user_id = None
        if sign_in_request.ok:
            sign_in_data = json.loads(sign_in_request.content.decode())
            id_token = sign_in_data['idToken']
            user_id = sign_in_data['localId']
            refresh_token = sign_in_data['refreshToken']

            Auth.sign_in_with_tokens(id_token, refresh_token, user_id)
        return user_id

    @staticmethod
    def sign_up(mail, password, name, phonenumber):
        """
        Creates an account with the given data. Saves to firebase. Doesn't sign in.
        :param mail: A valid mail
        :param password: A valid password at least 8 in length
        :param name: The name of the new user
        :param phonenumber: The phonenumber of the new user
        :return: The user id for the new user
        """
        sign_up_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + webApiKey
        sign_up_payload = {
            "email": mail,
            "password": password,
            "returnSecureToken": True
        }
        sign_up_request = requests.post(sign_up_url, data=sign_up_payload)

        if sign_up_request.ok:
            sign_up_data = json.loads(sign_up_request.content.decode())
            token = sign_up_data['idToken']
            refresh_token = sign_up_data['refreshToken']
            user_id = sign_up_data['localId']

            Auth.sign_in_with_tokens(token, refresh_token, user_id)

            with Firestore.batch("users") as batch:
                batch.set(
                    user_id, {
                        "mail": mail,
                        "name": name,
                        "phonenumber": phonenumber,
                        "avatar": "",
                        "balance": 0,
                        "rating": 0,
                    })

        else:
            error_data = json.loads(sign_up_request.content.decode())
            error_message = error_data["error"]['message']
            print(error_data)
            print(error_message)
            if error_message == "EMAIL_EXISTS":
                print("This mail is already registered")

    @staticmethod
    def sign_out():
        """
        Signs out from UserMeGetter and clears credential store.
        :return:
        """
        UserMeGetter.set_me("")
        credential_store.delete("tokens")
