from typing import Dict, Union

from model.delivery_request import DeliveryRequest
from model.firebase.firestore import Firestore


class DeliveryRequestUploader:
    @staticmethod
    def request_to_dict(request: DeliveryRequest) -> Dict[str, Union[str, int, float, bool]]:
        req_dict = {}
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
        request_dict = DeliveryRequestUploader.request_to_dict(request)

        with Firestore.batch("packages") as batch:
            batch.create(request_dict)
