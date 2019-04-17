from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.button import MDIconButton, MDRaisedButton
from kivymd.list import ILeftBodyTouch, OneLineIconListItem
from kivy.metrics import dp
from kivy.clock import Clock
from model.delivery_request import DeliveryRequest

Builder.load_file("view/delivery_list.kv")

available_delivery_requests = [
    DeliveryRequest("Brunnsparken", "Frölunda Torg", reward=20, weight=0),
    DeliveryRequest("Brunnsparken", "Frölunda Torg", reward=20, weight=1),
    DeliveryRequest("Brunnsparken", "Frölunda Torg", reward=20, weight=2),
    DeliveryRequest("Brunnsparken", "Frölunda Torg", reward=20, weight=3),
    DeliveryRequest("Torslanda", "Chalmers", reward=30, weight=1),
    DeliveryRequest("Torslanda", "Chalmers", reward=40, weight=1),
    DeliveryRequest("Torslanda", "Chalmers", reward=50, weight=1),
    DeliveryRequest("Torslanda", "Chalmers", reward=60, weight=1),
]


class DeliveryList(BoxLayout):
    """
    Widget that lists all available delivery requests.

    Each request is represented with a ListItem.
    """

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(DeliveryList, self).__init__(**kwargs)
        Clock.schedule_once(self._init_content)

    def _init_content(self, delta_time):
        """Fill delivery list"""
        for req in available_delivery_requests:
            self.ids.list_content.add_widget(ListItem(req))


class WhiteCardButton(MDRaisedButton):
    """Widget that alters MDRaisedButton to a blank card-looking button with a drop shadow."""

    _radius = NumericProperty(dp(14))


class ListItem(WhiteCardButton):
    """Widget that represents all the content of a list item."""

    def __init__(self, delivery_request, **kwargs):
        """Initializes the delivery list"""
        super(ListItem, self).__init__(**kwargs)
        self.ids.origin.text = delivery_request.origin
        self.ids.destination.text = delivery_request.destination
        self.ids.distance.text = delivery_request.get_distance_pretty()
        self.ids.reward.text = str(delivery_request.reward)
        self.ids.weight.text = delivery_request.weight_text
        self.ids.weight_icon.icon = delivery_request.weight_icon


class HollowIcon(ILeftBodyTouch, MDIconButton):
    """
    An icon that can't be interacted with.

    Events are instead passed through to the underlying widget.
    """

    def on_release(self, *args):  # noqa: D102
        pass

    def on_touch_down(self, *args):  # noqa: D102
        pass

    def on_touch_move(self, *args):  # noqa: D102
        pass

    def on_touch_up(self, *args):  # noqa: D102
        pass


class IconWithText(OneLineIconListItem):
    """A left-aligned icon with some text to the right. Non-interactable."""

    divider = None

    def on_release(self, *args):  # noqa: D102
        pass

    def on_touch_down(self, *args):  # noqa: D102
        pass

    def on_touch_move(self, *args):  # noqa: D102
        pass

    def on_touch_up(self, *args):  # noqa: D102
        pass
