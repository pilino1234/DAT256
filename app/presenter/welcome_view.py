from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("view/welcome_view.kv")


class WelcomeView(BoxLayout):
    deliver_button_callback = ObjectProperty(lambda: print("deliver_button_callback"))
    request_delivery_button_callback = ObjectProperty(lambda: print("request_delivery_button_callback"))

