from model.delivery_request import DeliveryRequest, Status
from model.location import Location
from model.minified_user import MinifiedUser


def create_delivery_request():
    origin = Location(name="Odenvägen 1, SE-194 63 Odenslunda, Sweden",
                      latitude=59.51224,
                      longitude=17.93536).to_dict()
    destination = Location(name="Rolsmo 1, SE-360 24 Linneryd, Sweden",
                           latitude=56.64989,
                           longitude=15.16624).to_dict()
    return DeliveryRequest(
        "TEST",
        "item",
        "This a test, feel free to remove.",
        origin,
        destination,
        reward=10,
        weight=2,
        fragile=True,
        status=Status.AVAILABLE,
        money_lock=0,
        owner=MinifiedUser("", "", "",
                           "94MTAsYEcpTBGW98MQbjyuGEPUx1").to_dict(),
        assistant=MinifiedUser("", "", "", "").to_dict(),
        image_path="")
