from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.elevationbehavior import RectangularElevationBehavior

Builder.load_file("view/card.kv")


class Card(ButtonBehavior, RectangularElevationBehavior, BoxLayout):
    """A simple material design card on which you can put some content"""

    bg_color = ListProperty([1, 1, 1, 1])
    radius = NumericProperty(dp(2))
