from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from presenter.widget.calculator import CalculatorWidget

Builder.load_file("view/math.kv")


class MathScreen(Screen):
    def __init__(self, **kwargs):
        super(MathScreen, self).__init__(**kwargs)
        widget = CalculatorWidget()
        self.add_widget(widget)
