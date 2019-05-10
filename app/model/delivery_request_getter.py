from typing import Text, Any, List

from model.delivery_request import DeliveryRequest, Status
from model.firebase.firestore import Firestore


class DeliveryRequestGetter:
    """
    A class for handling operations related to uploading delivery requests.

    Contains:
    ---------
        Converter for converting a DeliveryRequest object to a dict for uploading
        Uploader for uploading a delivery request to Firebase
    """

    @staticmethod
    def query(field_path: Text, op_str: Text,
              value: Any) -> List[DeliveryRequest]:
        """
        Get a list of DeliveryRequest objects by querying Firestore

        :param field_path: The path being filtered on.
        :param op_str: The comparison operation being made
        :param value: The value which each entry is being compared to.
        """
        docs = Firestore.get_raw('packages').where(field_path, op_str,
                                                   value).get()

        delivery_requests = []
        for doc in docs:
            data = doc.to_dict()
            data['uid'] = doc.id
            data['status'] = Status(data['status'])
            delivery_requests.append(DeliveryRequest(**data))

        return delivery_requests

    @staticmethod
    def get_by_id(delivery_request_id: Text) -> DeliveryRequest:
        """
        Get a specific DeliveryRequest from Firestore

        :param delivery_request_id: The id of the delivery request.
        """
        data = Firestore.get_raw('packages').document(
            delivery_request_id).get().to_dict()
        data['uid'] = delivery_request_id
        data['status'] = Status(data['status'])
        return DeliveryRequest(**data)
