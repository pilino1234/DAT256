from typing import Text, Optional

from model.delivery_request import DeliveryRequest, Status
from model.user import User
from model.firebase.firestore import Firestore
from model.user_getter import UserGetter


class UserMeGetter:
    """An helper class to maintain a user object that is streamed from Firebase"""

    _user_id: Text = ""
    user: Optional[User] = None

    @staticmethod
    def set_me(new_user_id: Text):
        """
        Sets up a new subscription for the given user id

        :param new_user_id: The signed in user
        """
        if UserMeGetter._user_id is not "":
            Firestore.unsubscribe(
                u'users/{user_id}/'.format(user_id=new_user_id))
            Firestore.unsubscribe(
                u'users/{user_id}/packages'.format(user_id=new_user_id))
            Firestore.unsubscribe(
                u'users/{user_id}/deliveries'.format(user_id=new_user_id))

        UserMeGetter._user_id = new_user_id

        if new_user_id != "":
            UserMeGetter.user = UserGetter.get_by_id(new_user_id)
            Firestore.subscribe_document("users", new_user_id,
                                         UserMeGetter._on_snapshot_user)
            Firestore.subscribe(
                u'users/{user_id}/packages'.format(user_id=new_user_id),
                UserMeGetter._on_snapshot_user_packages)
            Firestore.subscribe(
                u'users/{user_id}/deliveries'.format(user_id=new_user_id),
                UserMeGetter._on_snapshot_user_deliveries)

    @staticmethod
    def _on_snapshot_user(document_snapshot, _, __):
        """
        The callback for when the user object is updated in Firebase

        :param document_snapshot: The updated snapshot from firebase
        """
        if UserMeGetter.user is None:
            return
        document_dict = document_snapshot[0].to_dict()
        UserMeGetter.user.update(**document_dict)

    @staticmethod
    def _on_snapshot_user_packages(collection_snapshot, _, __):
        """
        The callback for when the users packages are updated in Firebase

        :param collection_snapshot: The packages for the user
        """
        if UserMeGetter.user is None:
            return
        delivery_requests = []
        for doc in collection_snapshot:
            data = doc.to_dict()
            data['uid'] = doc.id
            data['status'] = Status(data['status'])
            delivery_requests.append(DeliveryRequest(**data))

        UserMeGetter.user.update(packages=delivery_requests)

    @staticmethod
    def _on_snapshot_user_deliveries(collection_snapshot, _, __):
        """
        The callback for when the users deliveries are updated in Firebase

        :param collection_snapshot: The deliveries for the user
        """
        if UserMeGetter.user is None:
            return
        delivery_requests = []
        for doc in collection_snapshot:
            data = doc.to_dict()
            data['uid'] = doc.id
            data['status'] = Status(data['status'])
            delivery_requests.append(DeliveryRequest(**data))

        UserMeGetter.user.update(deliveries=delivery_requests)
