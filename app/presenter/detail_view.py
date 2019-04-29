from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.button import MDRaisedButton

from model.delivery_request import DeliveryRequest

Builder.load_file("view/detail_view.kv")

dummyRequest = DeliveryRequest("Package 2",
                               "Brunnsparken",
                               "Frölunda Torg",
                               reward=20,
                               weight=0,
                               fragile=False,
                               status=0,
                               money_lock=0)


class DetailView(BoxLayout):
    """Widget that shows details about a specific delivery request."""

    def __init__(self, request=dummyRequest, **kwargs):
        """Initializes a DetailView"""
        super(DetailView, self).__init__(**kwargs)
        self.request = request
        Clock.schedule_once(self._init_content)

    def accept_delivery_button_callback(self, button):
        """Callback function for the Show On Map button."""
        print("Got a callback from the accept delivery button!")

    def show_on_map_button_callback(self, button):
        """Callback function for the Show On Map button."""
        print("Got a callback from the show on map button!")

    def back_button_callback(self):
        """Callback function for the Back button."""
        print("Got a callback from the back button!")

    def _init_content(self, delta_time):
        """Initializes all the views content after it's been loaded."""
        self.ids.stack.add_widget(
            DetailLabel(title="Item", description=self.request.item))
        self.ids.stack.add_widget(
            DetailLabel(title="Origin", description=self.request.origin))
        self.ids.stack.add_widget(
            DetailLabel(title="Destination",
                        description=self.request.destination))
        self.ids.stack.add_widget(
            DetailLabel(title="Delivery Distance",
                        description=self.request.get_distance_pretty()))
        self.ids.stack.add_widget(
            DetailIcon(title="Weight",
                       icon=self.request.weight_icon,
                       size_hint_x=0.5))
        self.ids.stack.add_widget(
            DetailLabel(title="Fragile",
                        description="Yes" if self.request.fragile else "No",
                        size_hint_x=0.5))
        self.ids.stack.add_widget(
            DetailLabel(title="Reward",
                        description="$ " + str(self.request.reward),
                        size_hint_x=0.5))
        self.ids.stack.add_widget(
            DetailLabel(title="Money Lock",
                        description="$ " + str(self.request.money_lock),
                        size_hint_x=0.5))
        self.ids.stack.add_widget(
            DetailLabel(title="Description",
                        description="Some weird ass description!!!"))
        self.ids.stack.add_widget(
            MDRaisedButton(text="Show On Map",
                           size_hint=[0.5, None],
                           on_release=self.show_on_map_button_callback))
        self.ids.stack.add_widget(
            MDRaisedButton(text="Accept Delivery",
                           size_hint=[0.5, None],
                           on_release=self.accept_delivery_button_callback))


class DetailLabel(BoxLayout):
    """A pair of labels showing a title and a description for that title."""

    def __init__(self, title: str, description: str, **kwargs):
        """Initializes a DetailLabel."""
        super(DetailLabel, self).__init__(**kwargs)
        self.ids.title.text = title
        self.ids.description.text = description
        if 'size_hint_x' in kwargs:
            self.size_hint_x = kwargs['size_hint_x']


class DetailIcon(BoxLayout):
    """A pair of labels showing a title and an icon accompanying that title."""

    def __init__(self, title: str, icon: str, **kwargs):
        """Initializes a DetailIcon."""
        super(DetailIcon, self).__init__(**kwargs)
        self.ids.title.text = title
        self.ids.icon.icon = icon
        self.ids.icon.text_color = 107 / 255, 200 / 255, 0 / 255, 1
        if 'size_hint_x' in kwargs:
            self.size_hint_x = kwargs['size_hint_x']