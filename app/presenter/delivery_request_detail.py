from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from typing import Callable
from kivy.clock import Clock

from model.delivery_request import DeliveryRequest, Status
from model.firebase.firestore import Firestore
from model.user_getter import UserGetter
from model.user import User

from presenter.user_profile_view import UserProfileView

Builder.load_file("view/delivery_request_detail.kv")


class DeliveryRequestDetail(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    request = ObjectProperty(DeliveryRequest)
    delivery_assistant = ObjectProperty(User)
    _detail_view = ObjectProperty(None)
    _back_button_handler = ObjectProperty(None)

    def __init__(self, back_button_handler: Callable, request: DeliveryRequest,
                 **kwargs):
        """Initializes a DeliveryRequestDetail"""
        self.request = request
        self._back_button_handler = back_button_handler
        self.is_owner = self.request.owner == 'pIAeLAvHXp0KZKWDzTMz'
        super(DeliveryRequestDetail, self).__init__(**kwargs)
        self._detail_view = self.ids.detail_view.__self__
        self._setup_assistant_field()
        Clock.schedule_once(self._setup_action_button)

    def _setup_assistant_field(self):
        if self.request.assistant is not None and self.request.assistant != "":
            user = UserGetter.get_by_id(self.request.assistant)
        else:
            user = None

        if user is not None:
            self.ids.assistant.description = user.name
            self.ids.assistant.on_touch_up = self._transition_to_user_profile
            self.delivery_assistant = user
        else:
            self.ids.stack.remove_widget(self.ids.assistant)

    def _setup_action_button(self, _):
        if self.is_owner:
            if self.request.status == Status.ACCEPTED:
                self.ids.action_button.text = "Confirm Pickup"
                self.ids.action_button.on_release = self.confirm_pickup
            elif self.request.status == Status.TRAVELLING:
                self.ids.action_button.text = "Confirm Delivery"
                self.ids.action_button.on_release = self.confirm_delivery

        else:
            if self.request.status == Status.AVAILABLE:
                self.ids.action_button.text = "Accept Delivery"
                self.ids.action_button.on_release = self.accept_delivery

        if self.ids.action_button.text == "":
            self.ids.stack.remove_widget(self.ids.action_button)

    def accept_delivery(self):
        """Accept the delivery as the current user."""
        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.ACCEPTED,
                'assistant': u'pIAeLAvHXp0KZKWDzTMz'
            })
        self._back_button_handler()

    def confirm_pickup(self):
        """Confirm the delivery as picked up, as the current user."""
        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.TRAVELLING,
            })
        self._back_button_handler()

    def confirm_delivery(self):
        """
        Confirm the delivery as delivered, as the current user.

        Also withdraw money.
        """
        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.DELIVERED,
            })

        assistant_ref = Firestore.get_raw('users').document(
            self.request.assistant).get()
        assistant_balance = assistant_ref._data['balance']

        with Firestore.batch('users') as batch:
            batch.update(
                self.request.assistant, {
                    'balance':
                    assistant_balance + self.request.money_lock +
                    self.request.reward,
                })
        self._back_button_handler()

    def _transition_to_user_profile(self, touch):
        """Show the user profile of a specific user."""
        if self.ids.assistant.collide_point(*touch.pos):
            self.clear_widgets()
            self.add_widget(
                UserProfileView(
                    user=self.delivery_assistant,
                    back_button_handler=self._transition_to_detail_view))

    def _transition_to_detail_view(self):
        """Show the detail view."""
        self.clear_widgets()
        self.add_widget(self._detail_view)


class DetailLabel(BoxLayout):
    """A pair of labels showing a title and a description for that title."""

    pass


class DetailIcon(BoxLayout):
    """A pair of labels showing a title and an icon accompanying that title."""

    pass
