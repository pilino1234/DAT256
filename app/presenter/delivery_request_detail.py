from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivymd.button import MDRaisedButton
from kivy.metrics import dp
from kivymd.toast import toast
from typing import Callable

from model.delivery_request import DeliveryRequest, Status
from model.firebase.bucket import Bucket
from model.firebase.firestore import Firestore
from model.minified_user import MinifiedUser
from model.user_getter import UserGetter
from model.user_me_getter import UserMeGetter

from presenter.minified_user_profile_view import MinifiedUserProfileView

Builder.load_file("view/delivery_request_detail.kv")


class DeliveryRequestDetail(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    request = ObjectProperty(DeliveryRequest)
    delivery_assistant: MinifiedUser
    delivery_owner: MinifiedUser
    _detail_view = ObjectProperty(None)
    _back_button_handler = ObjectProperty(None)

    def __init__(self, back_button_handler: Callable, request: DeliveryRequest,
                 **kwargs):
        """Initializes a DeliveryRequestDetail"""
        self.request = request

        self.delivery_owner = request.owner

        self._back_button_handler = back_button_handler
        self.is_owner = self.delivery_owner.uid == UserMeGetter._user_id
        super(DeliveryRequestDetail, self).__init__(**kwargs)
        self._detail_view = self.ids.detail_view.__self__
        self._setup_user_fields()
        Clock.schedule_once(self._setup_ui)

    def _setup_user_fields(self):
        assistant_widget, owner_widget = self.ids.assistant, self.ids.owner

        if self.request.has_assistant():
            self.delivery_assistant = self.request.assistant
            assistant_widget.description = self.delivery_assistant.name
        else:
            owner_widget.size_hint_x = 1
            self.ids.stack.remove_widget(assistant_widget)

        owner_widget.description = self.delivery_owner.name

    def _setup_ui(self, _):
        image_source = Bucket.get_url(self.request.image_path)
        photo_widget = self.ids.product_photo
        button = MDRaisedButton(size_hint=(1, None))
        button_2 = MDRaisedButton(size_hint=(1, None))
        if image_source:
            photo_widget.source = image_source
        else:
            photo_widget.parent.remove_widget(photo_widget)

        if self.is_owner:

            if self.request.status == Status.AVAILABLE \
                or self.request.status == Status.ACCEPTED:
                button_2.text = "Cancel package"
                button_2.on_release = self.cancel_delivery_by_owner
            if self.request.status == Status.ACCEPTED:
                button.text = "Confirm Pickup"
                button.on_release = self.confirm_pickup
            elif self.request.status == Status.TRAVELLING:
                button.text = "Confirm Delivery"
                button.on_release = self.confirm_delivery

        else:
            if self.request.status == Status.AVAILABLE:
                button.text = "Accept Delivery"
                button.on_release = self.accept_delivery
            elif self.request.status == Status.ACCEPTED \
                    and self.request.assistant.uid == UserMeGetter._user_id:
                button.text = "Cancel delivery"
                button.on_release = self.cancel_delivery_by_assistant

        if button.text != "":
            self.ids.stack.add_widget(button)

        if button_2.text != "":
            self.ids.stack.add_widget(button_2)

        if button.text != "" and button_2.text != "":
            button.size_hint_x = 0.5
            button_2.size_hint_x = 0.5

    def cancel_delivery_by_owner(self):
        """Cancel delivery as the current user, the owner"""
        if self.request.status == Status.ACCEPTED:
            assistant_uid = self.request.assistant.uid
            assistant = UserGetter.get_by_id(assistant_uid)
            with Firestore.batch('users') as batch:
                batch.update(
                    assistant_uid,
                    {'balance': assistant.balance + self.request.money_lock})

        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.CANCELLED_BY_OWNER,
                'assistant': {}
            })
        pass

    def cancel_delivery_by_assistant(self):
        """Cancel delivery as the current user, the assistant"""
        assistant = UserMeGetter.user

        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid,
                         {'status': Status.AVAILABLE,
                          'assistant': {}})

        with Firestore.batch('users') as batch:
            batch.update(
                UserMeGetter._user_id,
                {'balance': assistant.balance + self.request.money_lock})

        toast("Delivery cancelled by assistant")

    def accept_delivery(self):
        """Accept the delivery as the current user."""
        assistant_balance = UserMeGetter.user.balance
        assistant = UserMeGetter.user.to_minified()

        # Not enough money
        if assistant_balance < self.request.money_lock:
            return

        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.ACCEPTED,
                'assistant': assistant.to_dict()
            })

        with Firestore.batch('users') as batch:
            batch.update(
                assistant.uid,
                {'balance': assistant_balance - self.request.money_lock})

        toast("Delivery accepted. See my deliveries.")
        self._back_button_handler()

    def confirm_pickup(self):
        """Confirm the delivery as picked up, as the current user."""
        with Firestore.batch('packages') as batch:
            batch.update(self.request.uid, {
                'status': Status.TRAVELLING,
            })

        toast("Delivery picked up. Package is now traveling.")
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
            self.request.assistant.uid).get()
        assistant_balance = assistant_ref._data['balance']

        with Firestore.batch('users') as batch:
            batch.update(
                self.request.assistant.uid, {
                    'balance':
                    assistant_balance + self.request.money_lock +
                    self.request.reward,
                })

        toast("Package confirmed as delivered.")
        self._back_button_handler()

    def _transition_to_user_profile(self, user):
        """Show the user profile of a specific user."""
        self.clear_widgets()
        self.add_widget(
            MinifiedUserProfileView(
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


class DetailImage(MDRaisedButton):
    """A pair of labels showing a title and an icon accompanying that title."""

    title = StringProperty()
    source = StringProperty()
    _radius = NumericProperty(dp(14))
    md_bg_color_disabled = [1, 1, 1, 1]
    md_bg_color_down = [1, 1, 1, 1]

    def _get_md_bg_color_disabled(self):
        """Override super class' behavior for this particular action."""
        return 1, 1, 1, 1

    def on_disabled(self, instance, value):
        """Override super class' behavior for this particular action."""
        self.elevation = self.elevation_normal
