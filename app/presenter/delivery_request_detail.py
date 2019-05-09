from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.delivery_request import Status
from model.delivery_request_getter import DeliveryRequestGetter
from model.firebase.firestore import Firestore

Builder.load_file("view/delivery_request_detail.kv")

dummy_request = DeliveryRequestGetter.get_by_id(u'kMiNT8FkY1rtyg6ou7Pg')

class DeliveryRequestDetail(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    request = ObjectProperty(DeliveryRequest)
    back_button_handler = ObjectProperty(None)

    def __init__(self, request=dummy_request, **kwargs):
        """Initializes a DeliveryRequestDetail"""
        super(DeliveryRequestDetail, self).__init__(**kwargs)
        self.request = request
        self.back_button_handler = back_button_handler
        super(DetailView, self).__init__(**kwargs)

    def accept_delivery_button_callback(self):
        """Callback function for the Accept Delivery button."""
        with Firestore.batch('packages') as batch:
            batch.update(u'kMiNT8FkY1rtyg6ou7Pg', {'status': Status.ACCEPTED})
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
