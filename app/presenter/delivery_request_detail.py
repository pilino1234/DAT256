from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivymd.button import MDRaisedButton
from kivy.metrics import dp
from typing import Callable

from model.delivery_request import DeliveryRequest, Status
from model.firebase.firestore import Firestore
from model.user_getter import UserGetter

from presenter.user_profile_view import UserProfileView

Builder.load_file("view/delivery_request_detail.kv")


class DeliveryRequestDetail(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    request = ObjectProperty(DeliveryRequest)
    delivery_assistant = ObjectProperty(None)
    delivery_owner = ObjectProperty(None)
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
        self._setup_user_fields()
        self._setup_action_button()

    def _setup_user_fields(self):
        assistant, owner = (UserGetter.get_by_id(uid)
                            for uid in (self.request.assistant,
                                        self.request.owner))
        assistant_widget, owner_widget = self.ids.assistant, self.ids.owner
        if None in (assistant, owner):
            assistant_widget.size_hint_x = 1
            owner_widget.size_hint_x = 1

        if assistant is not None:
            assistant_widget.description = assistant.name
            self.delivery_assistant = assistant
        else:
            self.ids.stack.remove_widget(assistant_widget)

        if owner is not None:
            owner_widget.description = owner.name
            self.delivery_owner = owner
        else:
            self.ids.stack.remove_widget(owner_widget)

    def _setup_action_button(self):
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
        assistant = 'pIAeLAvHXp0KZKWDzTMz'
        assistant_ref = Firestore.get_raw('users').document(assistant).get()
        assistant_balance = assistant_ref._data['balance']

        # Not enough money
        if assistant_balance < self.request.money_lock:
            return

        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.ACCEPTED,
                'assistant': assistant
            })

        with Firestore.batch('users') as batch:
            batch.update(
                assistant,
                {'balance': assistant_balance - self.request.money_lock})

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

    def _transition_to_user_profile(self, user):
        """Show the user profile of a specific user."""
        self.clear_widgets()
        self.add_widget(
            UserProfileView(
                user=user,
                back_button_handler=self._transition_to_detail_view))

    def _transition_to_detail_view(self):
        """Show the detail view."""
        self.clear_widgets()
        self.add_widget(self._detail_view)


class DetailLabel(MDRaisedButton):
    """A pair of labels showing a title and a description for that title."""

    title = StringProperty()
    description = StringProperty()
    _radius = NumericProperty(dp(14))
    md_bg_color_disabled = [1, 1, 1, 1]
    md_bg_color_down = [1, 1, 1, 1]

    def _get_md_bg_color_disabled(self):
        """Override super class' behavior for this particular action."""
        return 1, 1, 1, 1

    def on_disabled(self, instance, value):
        """Override super class' behavior for this particular action."""
        self.elevation = self.elevation_normal


class DetailIcon(MDRaisedButton):
    """A pair of labels showing a title and an icon accompanying that title."""

    title = StringProperty()
    icon = StringProperty()
    _radius = NumericProperty(dp(14))
    md_bg_color_disabled = [1, 1, 1, 1]
    md_bg_color_down = [1, 1, 1, 1]

    def _get_md_bg_color_disabled(self):
        """Override super class' behavior for this particular action."""
        return 1, 1, 1, 1

    def on_disabled(self, instance, value):
        """Override super class' behavior for this particular action."""
        self.elevation = self.elevation_normal
