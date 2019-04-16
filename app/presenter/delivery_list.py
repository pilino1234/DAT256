from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.button import MDIconButton, MDRaisedButton
from kivymd.list import ILeftBodyTouch, OneLineIconListItem
from kivy.metrics import dp

Builder.load_file("view/delivery_list.kv")


class DeliveryList(BoxLayout):
    """
    Widget that lists all available delivery requests.

    Each request is represented with a ListItem.
    """

    pass


class WhiteCardButton(MDRaisedButton):
    """Widget that alters MDRaisedButton to a blank card-looking button with a drop shadow."""

    _radius = NumericProperty(dp(14))


class ListItem(WhiteCardButton):
    """Widget that represents all the content of a list item."""

    pass


class HollowIcon(ILeftBodyTouch, MDIconButton):
    """
    An icon that can't be interacted with.

    Events are instead passed through to the underlying widget.
    """

    def on_release(self, *args):  # noqa: D102
        pass

    def on_touch_down(self, *args):  # noqa: D102
        pass

    def on_touch_move(self, *args):  # noqa: D102
        pass

    def on_touch_up(self, *args):  # noqa: D102
        pass


class IconWithText(OneLineIconListItem):
    """A left-aligned icon with some text to the right. Non-interactable."""

    divider = None

    def on_release(self, *args):  # noqa: D102
        pass

    def on_touch_down(self, *args):  # noqa: D102
        pass

    def on_touch_move(self, *args):  # noqa: D102
        pass

    def on_touch_up(self, *args):  # noqa: D102
        pass
