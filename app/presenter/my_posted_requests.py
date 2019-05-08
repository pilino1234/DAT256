from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from model.delivery_request import DeliveryRequest, Status
from presenter.delivery_list import WhiteCardButton

from model.firebase.firestore import Firestore

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
        Firestore.subscribe("packages", lambda a, b, c: self._update_content())

    def _update_content(self):
        """Fech my deliveries"""
        docs = Firestore.get_raw('packages').where(u'owner', u'==', u'pIAeLAvHXp0KZKWDzTMz').get()

        delivery_requests = []
        for doc in docs:
            data = doc.to_dict()
            data['status'] = Status(data.get('status'))
            delivery_requests.append(DeliveryRequest(**data))

        """Fill delivery list"""
        self.ids.my_requests.clear_widgets()
        for req in delivery_requests:
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
