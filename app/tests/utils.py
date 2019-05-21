from model.delivery_request import DeliveryRequest, Status
from model.location import Location


def create_delivery_request():
    origin = ("Odenvägen 1, SE-194 63 Odenslunda, Sweden", 59.51224, 17.93536)
    destination = Location("Rolsmo 1, SE-360 24 Linneryd, Sweden", 56.64989,
                           15.16624)
    return DeliveryRequest("TEST",
                           "item",
                           "This a test, feel free to remove.",
                           origin,
                           destination,
                           reward=10,
                           weight=2,
                           fragile=True,
                           status=Status.AVAILABLE,
                           money_lock=0,
                           owner='person A',
                           assistant='person B',
                           image_path="")
