from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from model.delivery_request_getter import DeliveryRequestGetter
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
        """Fech my deliveries I have accepted"""
        delivery_requests = DeliveryRequestGetter.query(
            u'assistant', u'==', u'pIAeLAvHXp0KZKWDzTMz')

        # Fill delivery list
        self.ids.my_deliveries.clear_widgets()
        for req in delivery_requests:
            self.ids.my_deliveries.add_widget(ListItem(req))
