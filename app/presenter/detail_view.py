from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from model.delivery_request import DeliveryRequest
from typing import Callable

Builder.load_file("view/detail_view.kv")


class DetailView(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    request = ObjectProperty(DeliveryRequest)
    back_button_handler = ObjectProperty(None)

    def __init__(self, back_button_handler: Callable, request: DeliveryRequest,
                 **kwargs):
        """Initializes a DetailView"""
        self.request = request
        self.back_button_handler = back_button_handler
        super(DetailView, self).__init__(**kwargs)

    def accept_delivery_button_callback(self):
        """Callback function for the Show On Map button."""
        print("Got a callback from the accept delivery button!")

    def show_on_map_button_callback(self):
        """Callback function for the Show On Map button."""
        print("Got a callback from the show on map button!")


class DetailLabel(BoxLayout):
    """A pair of labels showing a title and a description for that title."""

    pass


class DetailIcon(BoxLayout):
    """A pair of labels showing a title and an icon accompanying that title."""

    pass
