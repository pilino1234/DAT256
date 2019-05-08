from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from model.delivery_request import DeliveryRequest, Status
from presenter.delivery_list import WhiteCardButton

from model.firebase.firestore import Firestore

Builder.load_file("view/my_posted_requests.kv")

_delivery_requests = []

docs = Firestore.get_raw('packages').where(u'owner', u'==', u'pIAeLAvHXp0KZKWDzTMz').get()
for doc in docs:
    data = doc.to_dict()
    data['status'] = Status(data.get('status'))
    _delivery_requests.append(DeliveryRequest(**data))

class MyPostedRequests(BoxLayout):
    """
    Widget that lists all delivery requests owned by the user.

    Each request is represented with a ListItem.
    """

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(MyPostedRequests, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, delta_time):
        """Fill delivery list"""
        for req in _delivery_requests:
            self.ids.my_requests.add_widget(MyPostedRequest(req))


class MyPostedRequest(WhiteCardButton):
    """Widget that represents all the content of a list item."""

    def __init__(self, delivery_request, **kwargs):
        """Initializes the delivery list"""
        super(MyPostedRequest, self).__init__(**kwargs)
        self.ids.item.text = delivery_request.item
        self.ids.origin.text = delivery_request.origin
        self.ids.destination.text = delivery_request.destination
        self.ids.reward.text = delivery_request.reward_pretty
        self.ids.status.text = "Status: " + delivery_request.status_text
