from kivy.lang import Builder
from kivy.properties import NumericProperty, OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.button import MDIconButton, MDRoundFlatButton, MDRaisedButton
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, OneLineIconListItem
from kivy.metrics import dp


Builder.load_file("view/delivery_list.kv")


class GoodButton(MDRaisedButton):
    _radius = NumericProperty(dp(18))

    def lay_canvas_instructions(self):
        with self.canvas.after:
            StencilPush()
            RoundedRectangle(size=self.size,
                             pos=self.pos,
                             radius=[self._radius, ])
            StencilUse()
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse =\
                Ellipse(size=(self.ripple_rad, self.ripple_rad),
                        pos=(self.ripple_pos[0] - self.ripple_rad / 2.,
                             self.ripple_pos[1] - self.ripple_rad / 2.))
            StencilUnUse()
            RoundedRectangle(size=self.size,
                             pos=self.pos,
                             radius=[self._radius, ])
            StencilPop()
        self.bind(ripple_color=self._set_color, ripple_rad=self._set_ellipse)

class DeliveryList(BoxLayout):
    pass

class ListItem(GoodButton):
    _radius = NumericProperty(14)
    pass

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class IconWithText(OneLineIconListItem):
    divider = None

    def on_release(self, *args):
        pass

    def on_touch_down(self, *args):
        pass

    def on_touch_move(self, *args):
        pass

    def on_touch_up(self, *args):
        pass

