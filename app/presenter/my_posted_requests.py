from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from typing import Callable

from model.delivery_request import DeliveryRequest
from model.delivery_request_getter import DeliveryRequestGetter
from model.firebase.firestore import Firestore
from presenter.delivery_list import WhiteCardButton
from presenter.delivery_request_detail import DeliveryRequestDetail

Builder.load_file("view/my_posted_requests.kv")


class MyPostedRequests(BoxLayout):
    """
    Widget that lists all delivery requests owned by the user.

    Each request is represented with a ListItem.
    """

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(MyPostedRequests, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self._update_content())
        Firestore.subscribe("packages", lambda *_: self._update_content())

    def _update_content(self):
        """Fetch my posted deliveries"""
        self.content = self.ids.content
        delivery_requests = DeliveryRequestGetter.query(
            u'owner', u'==', u'pIAeLAvHXp0KZKWDzTMz')

        # Fill delivery list
        self.ids.my_requests.clear_widgets()
        for req in delivery_requests:
            self.ids.my_requests.add_widget(
                MyPostedRequest(req, self._transition_to_detail_view))

    def _transition_to_detail_view(self, request: DeliveryRequest):
        """Show detail view for selected delivery request."""
        self.clear_widgets()
        self.add_widget(
            DeliveryRequestDetail(
                back_button_handler=self._transition_to_delivery_list,
                request=request))

    def _transition_to_delivery_list(self):
        """Show list of all available deliveries."""
        self.clear_widgets()
        self.add_widget(self.content)


class MyPostedRequest(WhiteCardButton):
    """Widget that represents all the content of a list item."""

    tap_callback = ObjectProperty(None)
    request = ObjectProperty(None)

    def __init__(self, delivery_request: DeliveryRequest,
                 tap_callback: Callable, **kwargs):
        """Initializes the delivery list"""
        super(MyPostedRequest, self).__init__(**kwargs)

        self.request = delivery_request
        self.tap_callback = tap_callback
        self.ids.item.text = delivery_request.item
        self.ids.origin.text = delivery_request.origin.name
        self.ids.destination.text = delivery_request.destination.name
        self.ids.reward.text = delivery_request.reward_pretty
        self.ids.status.text = "Status: " + delivery_request.status_text
