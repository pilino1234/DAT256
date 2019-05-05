from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from model.delivery_request import DeliveryRequest, Status
from presenter.delivery_list import WhiteCardButton

Builder.load_file("view/my_posted_requests.kv")

_delivery_requests = [
    DeliveryRequest("Package1",
                    "Some description.",
                    "Brunnsparken",
                    "Frölunda Torg",
                    reward=20,
                    weight=0,
                    fragile=False,
                    status=Status.AVAILABLE,
                    money_lock=0),
    DeliveryRequest("Package2",
                    "Some description.",
                    "Brunnsparken",
                    "Frölunda Torg",
                    reward=20,
                    weight=1,
                    fragile=False,
                    status=Status.ACCEPTED,
                    money_lock=0),
    DeliveryRequest("Package3",
                    "Some description.",
                    "Brunnsparken",
                    "Frölunda Torg",
                    reward=20,
                    weight=2,
                    fragile=True,
                    status=Status.TRAVELLING,
                    money_lock=0),
    DeliveryRequest("Package4",
                    "Some description.",
                    "Brunnsparken",
                    "Frölunda Torg",
                    reward=20,
                    weight=3,
                    fragile=False,
                    status=Status.DELIVERED,
                    money_lock=0),
    DeliveryRequest("Package5",
                    "Some description.",
                    "Torslanda",
                    "Chalmers",
                    reward=30,
                    weight=1,
                    fragile=False,
                    status=Status.AVAILABLE,
                    money_lock=0),
    DeliveryRequest("Package6",
                    "Some description.",
                    "Torslanda",
                    "Chalmers",
                    reward=40,
                    weight=1,
                    fragile=True,
                    status=Status.AVAILABLE,
                    money_lock=0),
    DeliveryRequest("Package7",
                    "Some description.",
                    "Torslanda",
                    "Chalmers",
                    reward=50,
                    weight=1,
                    fragile=True,
                    status=Status.AVAILABLE,
                    money_lock=0),
    DeliveryRequest("Package8",
                    "Some description.",
                    "Torslanda",
                    "Chalmers",
                    reward=60,
                    weight=1,
                    fragile=False,
                    status=Status.AVAILABLE,
                    money_lock=0),
]


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
        self.ids.origin.text = delivery_request.origin
        self.ids.destination.text = delivery_request.destination
        self.ids.reward.text = delivery_request.get_reward_pretty()
        self.ids.status.text = "Status: " + delivery_request.status_text
