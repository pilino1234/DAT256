from typing import Dict, Union

from model.delivery_request import DeliveryRequest
from model.firebase.firestore import Firestore


class DeliveryRequestUploader:
    @staticmethod
    def request_to_dict(request: DeliveryRequest) -> Dict[str, Union[str, int, float, bool]]:
        temp = {}
        temp.update({'item': request.item})
        temp.update({'description': request.description})
        temp.update({'origin': request.origin})
        temp.update({'destination': request.destination})
        temp.update({'reward': request.reward})
        temp.update({'weight': request.weight})
        temp.update({'fragile': request.fragile})
        temp.update({'status': request.status.value})
        temp.update({'money_lock': request.money_lock})

        return temp

    @staticmethod
    def upload(request: DeliveryRequest):
        request_dict = DeliveryRequestUploader.request_to_dict(request)

        with Firestore.batch("packages") as batch:
            batch.create(request_dict)
