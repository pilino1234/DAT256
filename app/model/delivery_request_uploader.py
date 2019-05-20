from model.delivery_request import DeliveryRequest
from model.firebase.firestore import Firestore


class DeliveryRequestUploader:
    """A class for handling operations related to uploading delivery requests."""

    @staticmethod
    def upload(request: DeliveryRequest):
        """
        Upload a delivery request to Firebase.

        :param request: The delivery request to upload.
        :type request: DeliveryRequest
        """
        request_dict = request.to_dict()

        with Firestore.batch("packages") as batch:
            batch.create_with_random_id(request_dict)
