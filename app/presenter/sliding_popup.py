from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

Builder.load_file("view/sliding_popup.kv")


class SlidingPopup(FloatLayout):
    """Widget that displays a sliding popup"""

    def __init__(self, **kwargs):
        """Initializes the sliding popup"""
        super(SlidingPopup, self).__init__(**kwargs)
        self.bg: "BackgroundDim" = self.ids.background_dim
        self.bg.on_release = lambda: self.hide()
        self.card: Widget = self.ids.popup_card
        self._visible = False

    def show(self):
        """Show the popup"""
        self.bg.fade_in()
        self._visible = True
        Animation(top_hint=self.card.height_hint,
                  transition="out_elastic").start(self.card)

    def hide(self):
        """Hide the popup"""
        self.bg.fade_out()
        self._visible = False
        Animation(top_hint=0, transition="out_elastic").start(self.card)


class BackgroundDim(ButtonBehavior, Widget):
    """Widget that dims the background"""

    def fade_in(self):
        """Darken the background"""
        self.__show()
        Animation(opacity=0.75, transition="out_elastic").start(self)

    def fade_out(self):
        """Stop dimming the background"""
        anim = Animation(opacity=0, transition="out_cubic")
        anim.bind(on_complete=lambda *args: self.__hide())
        anim.start(self)

    def __show(self):
        self.top_hint = 1
        self.visible = True

    def __hide(self):
        self.top_hint = 0
        self.visible = False
