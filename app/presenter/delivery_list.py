from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.button import MDIconButton, MDRaisedButton
from kivymd.list import ILeftBodyTouch, OneLineIconListItem
from kivymd.updatespinner import MDUpdateSpinner

from typing import Callable

from presenter.delivery_request_detail import DeliveryRequestDetail

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_getter import DeliveryRequestGetter

Builder.load_file("view/delivery_list.kv")
Builder.load_file("view/filtering_delivery.kv")


class DeliveryList(BoxLayout):
    """
    Widget that lists all available delivery requests.

    Each request is represented with a ListItem.
    """

    delivery_list = ObjectProperty(BoxLayout)

    deliveries = []

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(DeliveryList, self).__init__(**kwargs)
        Clock.schedule_once(self._fill_content)

    def _fill_content(self, delta_time):
        delivery_requests = DeliveryRequestGetter.query(
            u'status', u'==', Status.AVAILABLE)

        for delivery_request in delivery_requests:
            list_item = ListItem(delivery_request,
                                 self._transition_to_detail_view)
            self.ids.available_requests.add_widget(list_item)
            self.deliveries.append(delivery_request)

        self.delivery_list = self.ids.delivery_list
        self.add_widget(Filter())

    def _filter_content(self, walk, bike, car, truck, fragile, distance):
        '''Filters the delivery list depending on checkboxes and distance'''
        delivery_requests = DeliveryRequestGetter.query(
            u'status', u'==', Status.AVAILABLE)
        self.ids.available_requests.clear_widgets()
        for delivery_request in delivery_requests:
            if self.passes_filter(delivery_request, walk, bike, car, truck, fragile, distance):
                list_item = ListItem(delivery_request,
                                     self._transition_to_detail_view)
                self.ids.available_requests.add_widget(list_item)

        self.delivery_list = self.ids.delivery_list

    def passes_filter(self, delivery_request, walk, bike, car, truck, fragile, distance):
        '''Filters the delivery list depending on checkboxes and distance'''
        if distance == "":
            distance = 99999999999999
        arr = [walk, bike, car, truck]
        print(arr[delivery_request.weight])

        if not arr[delivery_request.weight]:
            return False

        if delivery_request.fragile and not fragile:
            return False

        if delivery_request.distance_km > float(distance):
            return False

        return True



    def _update_content(self, spinner):
        self.tick = 0

        def close_spinner(interval):
            spinner.update = True

        Clock.schedule_once(close_spinner, 2)
        self.ids.available_requests.clear_widgets()
        self._fill_content(0)

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
        self.add_widget(self.delivery_list)


class WhiteCardButton(MDRaisedButton):
    """Widget that alters MDRaisedButton to a blank card-looking button with a drop shadow."""

    _radius = NumericProperty(dp(14))


class ListItem(WhiteCardButton):
    """Widget that represents all the content of a list item."""

    request = ObjectProperty(None)
    tap_callback = ObjectProperty(None)

    def __init__(self, delivery_request: DeliveryRequest,
                 tap_callback: Callable, **kwargs):
        """Initializes the delivery list"""
        super(ListItem, self).__init__(**kwargs)

        self.tap_callback = tap_callback
        self.request = delivery_request
        self.ids.item.text = delivery_request.item
        self.ids.origin.text = delivery_request.origin
        self.ids.destination.text = delivery_request.destination
        self.ids.distance.text = delivery_request.distance_pretty
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


class UpdateSpinner(MDUpdateSpinner):
    """MDUpdateSpinner, but only shows up when pulling downwards."""

    scroll = ObjectProperty()

    def on_touch_move(self, touch):
        """Modifies the base method so that the user must pull downards."""
        if self.scroll.scroll_y < 1:
            return

        dy = touch.push_attrs_stack[0][1][4]
        if touch.grab_current is self and not self._spinner_work and dy < 0.0:
            self._step += 18
            if self._step > dp(210):
                self._spinner_work = True
                self.start_anim_spinner()
                return
            self.ids.body_spinner.y -= 18

    def start_anim_spinner(self):
        """Modifies the base method so that the spinner stays a bit lower when updating."""
        spinner = self.ids.body_spinner
        Animation(y=spinner.y + 35, d=.8, t='out_elastic').start(spinner)

        def wait_updates(interval):
            if self.update:
                self.transform_hide_anim_spinner()
                Clock.unschedule(wait_updates)

        Clock.schedule_interval(wait_updates, .1)
        self.event_update(self)


class Filter(BoxLayout):
    pass
