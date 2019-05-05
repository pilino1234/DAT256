"""The entry point of the Carrepsa app"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemeManager

from presenter.delivery_request_form import DeliveryRequestForm
from presenter.navbar import NavBarWithFAB
from presenter.sliding_popup import SlidingPopup


class Carrepsa(App):
    """
    The main class of the Carrepsa app

    This class handles the initial construction of the interface.
    """

    theme_cls = ThemeManager(primary_palette="Blue")

    def build(self) -> FloatLayout:
        """
        Builds the root view of the application window

        :return: The root BoxLayout of the window
        """
        root = FloatLayout()
        sp = SlidingPopup()
        sp.card.add_widget(DeliveryRequestForm())
        root.add_widget(NavBarWithFAB(fab_callback=lambda: sp.show()))
        root.add_widget(sp)

        return root


if __name__ == '__main__':
    Carrepsa().run()
