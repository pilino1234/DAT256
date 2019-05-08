from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from model.delivery_request import DeliveryRequest, Status
from presenter.delivery_list import ListItem

from model.firebase.firestore import Firestore

Builder.load_file("view/my_deliveries.kv")

_delivery_requests = []

docs = Firestore.get_raw('packages').where(u'assistant', u'==', u'pIAeLAvHXp0KZKWDzTMz').get()
for doc in docs:
    data = doc.to_dict()
    data['status'] = Status(data.get('status'))
    _delivery_requests.append(DeliveryRequest(**data))

class MyDeliveries(BoxLayout):
    """
    Widget that lists all delivery requests accepted by the user.

    Each request is represented with a ListItem.
    """

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(MyDeliveries, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, delta_time):
        """Fill delivery list"""
        for req in _delivery_requests:
            self.ids.my_deliveries.add_widget(ListItem(req))
