from model.delivery_request import DeliveryRequest, Status


def create_delivery_request():
    return DeliveryRequest("TEST",
                           "item",
                           "This a test, feel free to remove.",
                           "origin",
                           "destination",
                           reward=10,
                           weight=2,
                           fragile=True,
                           status=Status.AVAILABLE,
                           money_lock=0,
                           owner='person A',
                           assistant='person B')
