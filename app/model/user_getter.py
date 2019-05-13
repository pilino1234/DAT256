from typing import Text, Optional

from model.user import User
from model.firebase.firestore import Firestore


class UserGetter:
    """
    A class for handling operations related to getting user profiles from firebase.

    Contains:
    ---------
        A method for fetching specific users by their id.
    """

    @staticmethod
    def get_by_id(user_id: Text) -> Optional[User]:
        """
        Get a specific User from Firestore

        :param user_id: The id of the user.
        """
        data = Firestore.get_raw('users').document(user_id).get().to_dict()
        if data is not None:
            return User(**data)
        else:
            return None
