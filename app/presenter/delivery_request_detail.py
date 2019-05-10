from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from typing import Callable

from model.delivery_request import DeliveryRequest, Status
from model.firebase.firestore import Firestore

Builder.load_file("view/delivery_request_detail.kv")


class DeliveryRequestDetail(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    request = ObjectProperty(DeliveryRequest)
    back_button_handler = ObjectProperty(None)

    def __init__(self, back_button_handler: Callable, request: DeliveryRequest,
                 **kwargs):
        """Initializes a DeliveryRequestDetail"""
        self.request = request
        self.back_button_handler = back_button_handler
        super(DeliveryRequestDetail, self).__init__(**kwargs)

    def accept_delivery_button_callback(self):
        """Callback function for the Accept Delivery button."""
        # Can't accept your own request.
        if self.request.assistant == 'pIAeLAvHXp0KZKWDzTMz':
            return

        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.ACCEPTED,
                'assistant': u'pIAeLAvHXp0KZKWDzTMz'
            })

    def show_on_map_button_callback(self):
        """Callback function for the Show On Map button."""
        print("Got a callback from the show on map button!")


class DetailLabel(BoxLayout):
    """A pair of labels showing a title and a description for that title."""

    pass


class DetailIcon(BoxLayout):
    """A pair of labels showing a title and an icon accompanying that title."""

    pass
