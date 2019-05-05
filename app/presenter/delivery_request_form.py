from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.button import MDIconButton

Builder.load_file("view/delivery_request.kv")


class DeliveryRequestForm(BoxLayout):
    """Widget to create a delivery request"""

    weight = 2

    _weights = [
        'weight_walk_button', 'weight_bike_button', 'weight_car_button',
        'weight_truck_button'
    ]

    def __init__(self, **kwargs):
        """Instantiate a form for submitting a delivery request."""
        super(DeliveryRequestForm, self).__init__(**kwargs)
        for button_id in self._weights:
            button: MDIconButton = self.ids[button_id]

            button.bind(
                on_press=lambda _, bid=button_id: self._set_weight(bid))

        self._set_weight(self._weights[self.weight])

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
