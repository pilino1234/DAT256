from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from model.delivery_request import DeliveryRequest, Status

Builder.load_file("view/detail_view.kv")

dummyRequest = DeliveryRequest(
    item="Package 2",
    description="Lorem ipsum description goes here.",
    origin="Brunnsparken",
    destination="Frölunda Torg",
    reward=20,
    weight=0,
    fragile=False,
    status=Status.AVAILABLE,
    money_lock=0)


class DetailView(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    def __init__(self, request=dummyRequest, **kwargs):
        """Initializes a DetailView"""
        super(DetailView, self).__init__(**kwargs)
        self.request = request

    def accept_delivery_button_callback(self):
        """Callback function for the Show On Map button."""
        print("Got a callback from the accept delivery button!")

    def show_on_map_button_callback(self):
        """Callback function for the Show On Map button."""
        print("Got a callback from the show on map button!")

    def back_button_callback(self):
        """Callback function for the Back button."""
        print("Got a callback from the back button!")


class DetailLabel(BoxLayout):
    """A pair of labels showing a title and a description for that title."""

    pass


class DetailIcon(BoxLayout):
    """A pair of labels showing a title and an icon accompanying that title."""

    pass
