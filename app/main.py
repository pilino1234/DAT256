"""The entry point of the Carrepsa app"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager

from presenter.navbar import NavBarWithFAB


class Carrepsa(App):
    """
    The main class of the Carrepsa app

    This class handles the initial construction of the interface.
    """

    theme_cls = ThemeManager(primary_palette="Blue")

    def build(self) -> BoxLayout:
        """
        Builds the root view of the application window

        :return: The root BoxLayout of the window
        """
        root = BoxLayout()
        root.add_widget(
            NavBarWithFAB(fab_callback=lambda: print("FAB pressed!")))
        return root


if __name__ == '__main__':
    Carrepsa().run()
