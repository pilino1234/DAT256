from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("view/welcome_view.kv")


class WelcomeView(BoxLayout):
    """
    The view that welcomes new users

    This view welcomes new users and helps
    them get to different parts of the app
    depending on if they want to deliver
    packages or request deliveries.
    """

    deliver_button_callback = ObjectProperty(lambda: print(
        "deliver_button_callback"))
    request_delivery_button_callback = ObjectProperty(lambda: print(
        "request_delivery_button_callback"))
