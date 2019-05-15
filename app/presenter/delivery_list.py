from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivymd.button import MDIconButton, MDRaisedButton
from kivymd.list import ILeftBodyTouch, OneLineIconListItem
from kivymd.updatespinner import MDUpdateSpinner
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.app import App

from typing import Callable

from model.firebase.firestore import Firestore
from presenter.delivery_request_detail import DeliveryRequestDetail
from presenter.utils.suggester import LocationSuggester

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_getter import DeliveryRequestGetter

Builder.load_file("view/delivery_list.kv")
Builder.load_file("view/filtering_delivery.kv")


class DeliveryList(RelativeLayout):
    """
    Widget that lists all available delivery requests.

    Each request is represented with a ListItem.
    """

    delivery_list = ObjectProperty(BoxLayout)
    deliveries = [None]
    filter_widget = None
    previous_search_params = None

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(DeliveryList, self).__init__(**kwargs)
        self.filter_widget = Filter()
        if App.get_running_app().is_authenticated:
            Clock.schedule_once(self._filter_content)

    def _filter_content(self, walk, car, truck, fragile):
        """Filters the delivery list."""
        self.previous_search_params = [walk, car, truck, fragile]
        delivery_requests = DeliveryRequestGetter.query(
            u'status', u'==', Status.AVAILABLE)

        origin = self.filter_widget.from_suggester.currently_used_suggestion
        destination = self.filter_widget.to_suggester.currently_used_suggestion

        self.ids.available_requests.clear_widgets()
        for delivery_request in delivery_requests:
            if self.passes_filter(delivery_request, walk, car, truck, fragile,
                                  origin, destination):
                list_item = ListItem(delivery_request,
                                     self._transition_to_detail_view)
                self.ids.available_requests.add_widget(list_item)

        self.delivery_list = self.ids.delivery_list

        self.hide_filter()

    def passes_filter(self, delivery_request, walk, car, truck, fragile,
                      origin, destination):
        """Checks if a delivery request passes the filter."""
        checks = [walk, car, truck]

        # Pass checkboxes
        if not checks[delivery_request.weight]:
            return False

        # Matches fragile
        if delivery_request.fragile and not fragile:
            return False

        if origin is not None and not delivery_request.origin.is_close_to(
                origin):
            return False

        if destination is not None and not delivery_request.destination.is_close_to(
                destination):
            return False

        return True

    def _update_content(self, spinner):
        self.tick = 0

        def close_spinner(interval):
            spinner.update = True

        Clock.schedule_once(close_spinner, 2)
        self.ids.available_requests.clear_widgets()
        self._filter_content(*self.previous_search_params)

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

    def show_filter(self):
        """Show the filter widget"""
        self.ids.available_requests.clear_widgets()
        self.add_widget(self.filter_widget)

    def hide_filter(self):
        """Hide the filter widget"""
        self.remove_widget(self.filter_widget)


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
        self.ids.origin.text = delivery_request.origin.name
        self.ids.destination.text = delivery_request.destination.name
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
    """The filter widget"""

    from_suggester = None
    to_suggester = None

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(Filter, self).__init__(**kwargs)
        Clock.schedule_once(lambda x: self._init_content())

    def _init_content(self):
        self.from_suggester = LocationSuggester(self.ids.input_from)
        self.to_suggester = LocationSuggester(self.ids.input_to)
        self._update_search_button()

    def _on_search_from(self):
        if self.from_suggester is not None:
            self.from_suggester.on_search()
            self._update_search_button()

    def _on_search_to(self):
        if self.to_suggester is not None:
            self.to_suggester.on_search()
            self._update_search_button()

    def _update_search_button(self):
        from_ok = self.from_suggester.currently_used_suggestion is not None
        to_ok = self.to_suggester.currently_used_suggestion is not None
        enable = not (from_ok or to_ok)
        self.ids.search_button.disabled = enable
