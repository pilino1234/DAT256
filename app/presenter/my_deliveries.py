from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.delivery_request import DeliveryRequest
from model.delivery_request_getter import DeliveryRequestGetter
from presenter.delivery_request_detail import DeliveryRequestDetail
from model.firebase.firestore import Firestore
from presenter.delivery_list import ListItem

Builder.load_file("view/my_deliveries.kv")


class MyDeliveries(BoxLayout):
    """
    Widget that lists all delivery requests accepted by the user.

    Each request is represented with a ListItem.
    """

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(MyDeliveries, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self._update_content())
        Firestore.subscribe("packages", lambda *_: self._update_content())

    def _update_content(self):
        """Fetch all deliveries the current owner has accepted"""
        delivery_requests = DeliveryRequestGetter.query(
            u'assistant', u'==', u'pIAeLAvHXp0KZKWDzTMz')

        # Fill delivery list
        self.ids.my_deliveries.clear_widgets()
        for req in delivery_requests:
            self.ids.my_deliveries.add_widget(
                ListItem(req, self._transition_to_detail_view))

        self.content = self.ids.content

    def _transition_to_detail_view(self, request: DeliveryRequest):
        """Show detail view for selected delivery request."""
        self.clear_widgets()
        self.add_widget(
            DeliveryRequestDetail(
                back_button_handler=self._transition_to_my_deliveries,
                request=request))

    def _transition_to_my_deliveries(self):
        """Show list of all available deliveries."""
        self.clear_widgets()
        self.add_widget(self.content)
