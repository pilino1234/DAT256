from typing import Text

from model.user import User
from model.firebase.firestore import Firestore
from model.user_getter import UserGetter


class UserMeGetter:

    _user_id: Text = ""
    user: User = None

    @staticmethod
    def set_me(new_user_id: Text):
        if UserMeGetter._user_id is not "":
            Firestore.unsubscribe("users/" + UserMeGetter._user_id)

        UserMeGetter._user_id = new_user_id
        if new_user_id is not "":
            Firestore.subscribe_document("users", new_user_id, UserMeGetter._on_snapshot_user)
            UserMeGetter.user = UserGetter.get_by_id(new_user_id)

    @staticmethod
    def _on_snapshot_user(document_snapshot, _, __):
        if UserMeGetter.user is None:
            return
        document_dict = document_snapshot[0].to_dict()
        UserMeGetter.user.update(**document_dict)
