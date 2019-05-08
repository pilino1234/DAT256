from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from model.delivery_request import DeliveryRequest, Status
from presenter.delivery_list import ListItem

from model.firebase.firestore import Firestore

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
        Firestore.subscribe("packages", lambda a, b, c: self._update_content())

    def _update_content(self):
        """Fech my deliveries I have accepted"""
        docs = Firestore.get_raw('packages').where(u'assistant', u'==', u'pIAeLAvHXp0KZKWDzTMz').get()

        delivery_requests = []
        for doc in docs:
            data = doc.to_dict()
            data['status'] = Status(data.get('status'))
            delivery_requests.append(DeliveryRequest(**data))

        """Fill delivery list"""
        self.ids.my_deliveries.clear_widgets()
        for req in delivery_requests:
            self.ids.my_deliveries.add_widget(ListItem(req))
