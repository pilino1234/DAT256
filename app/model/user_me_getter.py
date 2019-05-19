from kivy.app import App
from typing import Text, Optional

from model.user import User
from model.firebase.firestore import Firestore


class UserMeGetter:

    _user_id: Text = None
    user: User = User()

    @staticmethod
    def set_me(user_id: Text):
        if UserMeGetter._user_id is not None:
            Firestore.unsubscribe("users/" + UserMeGetter._user_id)

        UserMeGetter._user_id = user_id
        Firestore.subscribe_document("users", user_id, UserMeGetter._on_snapshot_user)

    @staticmethod
    def _on_snapshot_user(document_snapshot, _, __):
        document_dict = document_snapshot[0].to_dict()
        UserMeGetter.user.update(**document_dict)

        print(UserMeGetter.user)