"""The entry point of the Carrepsa app"""

from kivy.app import App
from kivymd.theming import ThemeManager


class CarrepsaApp(App):
    """
    The main class of the Carrepsa app

    This class handles the initial construction of the interface.
    """

    kv_directory = 'view'
    theme_cls = ThemeManager(primary_palette="Blue")
    is_authenticated = False


if __name__ == '__main__':
    CarrepsaApp().run()
