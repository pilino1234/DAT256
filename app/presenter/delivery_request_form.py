from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.button import MDIconButton
from kivymd.textfields import MDTextField

from presenter.user_profile_view import UserProfileView
from presenter.utils.suggester import LocationSuggester

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_uploader import DeliveryRequestUploader
from model.user import User

Builder.load_file("view/delivery_request_form.kv")


class DeliveryRequestForm(BoxLayout):
    """Widget to create a delivery request"""

    weight = 0
    from_suggester = None
    to_suggester = None

    _weights = [
        'weight_walk_button', 'weight_bike_button', 'weight_car_button',
        'weight_truck_button'
    ]

    __text_field_ids = [
        'package_name', 'description_text', 'from_text', 'dest_text',
        'payment_amount', 'money_lock_amount'
    ]

    def __init__(self, **kwargs):
        """Instantiate a form for submitting a delivery request."""
        super(DeliveryRequestForm, self).__init__(**kwargs)

        for button_id in self._weights:
            button: MDIconButton = self.ids[button_id]

            button.bind(
                on_press=lambda _, bid=button_id: self._set_weight(bid))

        self._set_weight(self._weights[self.weight])

        for text_id in self.__text_field_ids:
            text_field: MDTextField = self.ids[text_id]
            text_field.bind(text=self._verify_entries)

        Clock.schedule_once(lambda x: self._init_content())

    def _init_content(self):
        self.from_suggester = LocationSuggester(self.ids.from_text)
        self.to_suggester = LocationSuggester(self.ids.dest_text)

    def _set_weight_cb(self, button_id: str, _button: MDIconButton):
        self._set_weight(button_id)

    def _set_weight(self, button_id: str):
        prev_button_id = self._weights[self.weight]
        self.__unhighlight_weight_button(prev_button_id)

        self.weight = self._weights.index(button_id)
        self.__highlight_weight_button(button_id)

    def __unhighlight_weight_button(self, button_id: str):
        button: MDIconButton = self.ids[button_id]
        button.text_color = [128 / 255, 128 / 255, 128 / 255]

    def __highlight_weight_button(self, button_id: str):
        button: MDIconButton = self.ids[button_id]
        button.text_color = [50 / 255, 205 / 255, 50 / 255, 1]

    def _verify_entries(self, *_args) -> bool:
        """
        Verify the entries in the request form.

        :return: True if all inputs are valid
                 False otherwise
        """
        all_good = (len(self.ids.package_name.text) > 0
                    and len(self.ids.from_text.text) > 0
                    and len(self.ids.dest_text.text) > 0
                    and len(self.ids.payment_amount.text) > 0
                    and '-' not in self.ids.payment_amount.text
                    and int(self.ids.payment_amount.text) > 0
                    and len(self.ids.money_lock_amount.text) > 0
                    and '-' not in self.ids.money_lock_amount.text
                    and int(self.ids.money_lock_amount.text) >= 0)

        self.ids.request_button.disabled = not all_good
        return all_good

    def _clear_form(self):
        self.ids.package_name.text = ""
        self.ids.from_text.text = ""
        self.ids.dest_text.text = ""
        self.ids.payment_amount.text = ""
        self.ids.money_lock_amount.text = ""
        self.ids.description_text.text = ""
        self._set_weight(self._weights[2])
        self.ids.fragile_bool.active = False

    def _submit_request(self):
        payment_amount: int = int(self.ids.payment_amount.text)
        user: User = UserProfileView.user_me

        if payment_amount > user.balance:
            # User does not have enough money to pay for this delivery
            return

        origin = self.from_suggester.currently_used_suggestion
        destination = self.to_suggester.currently_used_suggestion

        # Both origin and destination must be well-defined
        if not origin or not destination:
            return

        request = DeliveryRequest(
            item=self.ids.package_name.text,
            description=self.ids.description_text.text,
            origin=origin,
            destination=destination,
            reward=payment_amount,
            weight=self.weight,
            fragile=self.ids.fragile_bool.active,
            status=Status.AVAILABLE,
            money_lock=int(self.ids.money_lock_amount.text),
            owner='pIAeLAvHXp0KZKWDzTMz',
            assistant='',
            uid='')

        user.lock_delivery_amount(request)

        DeliveryRequestUploader.upload(request)

        # Hide the sliding popup. We are placed in a SlidingPopupContent widget,
        # whose parent is the SlidingPopup we need.
        self.parent.parent.hide()

        self._clear_form()

    def _on_search_from(self):
        if self.from_suggester is not None:
            self.from_suggester.on_search()

    def _on_search_to(self):
        if self.to_suggester is not None:
            self.to_suggester.on_search()
