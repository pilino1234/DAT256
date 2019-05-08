from typing import Dict, Union

from model.delivery_request import DeliveryRequest
from model.firebase.firestore import Firestore


class DeliveryRequestUploader:
    """
    A class for handling operations related to uploading delivery requests.

    Contains:
    ---------
        Converter for converting a DeliveryRequest object to a dict for uploading
        Uploader for uploading a delivery request to Firebase
    """

    @staticmethod
    def _request_to_dict(request: DeliveryRequest
                         ) -> Dict[str, Union[str, float, int, bool]]:
        """
        Convert a DeliverRequest object to a dict ready for uploading.

        :param request: The DeliveryRequest to convert.
        :return: A dict that can be uploaded.
        :rtype: dict
        """
        req_dict: Dict[str, Union[str, float, int, bool]] = {}
        req_dict.update({'item': request.item})
        req_dict.update({'description': request.description})
        req_dict.update({'origin': request.origin})
        req_dict.update({'destination': request.destination})
        req_dict.update({'reward': request.reward})
        req_dict.update({'weight': request.weight})
        req_dict.update({'fragile': request.fragile})
        req_dict.update({'status': request.status.value})
        req_dict.update({'money_lock': request.money_lock})

        return req_dict

    @staticmethod
    def upload(request: DeliveryRequest):
        """
        Upload a delivery request to Firebase.

        :param request: The delivery request to upload.
        :type request: DeliveryRequest
        """
        request_dict = DeliveryRequestUploader._request_to_dict(request)

        with Firestore.batch("packages") as batch:
            batch.create(request_dict)
