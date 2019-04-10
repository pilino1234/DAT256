from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.label import MDLabel
from kivymd.theming import ThemeManager

from presenter.screen.main_menu import MainMenuScreen
from presenter.screen.math import MathScreen
from presenter.screen.settings import SettingsScreen
# App screens
from presenter.widget.navbar import NavBar

screen_manager = ScreenManager()
screen_manager.add_widget(MainMenuScreen(name='main_menu'))
screen_manager.add_widget(SettingsScreen(name='settings'))
screen_manager.add_widget(MathScreen(name='math'))
screen_manager.current = 'main_menu'

root = BoxLayout()


class Carrepsa(App):
    theme_cls = ThemeManager()

    def build(self):
        nav_bar = NavBar(
            fab_icon='package',
            fab_callback=lambda x: print("FAB pressed!"),
            fab_color=self.theme_cls.bg_light,
            tabs=[
                {
                    'title': "Map",
                    'icon': "map-marker",
                    'widget': MDLabel(text="Show the map here", halign='center')
                },
                {
                    'title': "My Packages",
                    'icon': "package",
                    'widget': MDLabel(text="List of my packages", halign='center')
                },
                {  # TODO Find a way to get spacing here without a dummy tab
                    'title': " ",
                    'icon': "box",
                    'widget': screen_manager
                },
                {
                    'title': "Deliver",
                    'icon': "car",
                    'widget': MDLabel(text="Delivery stuff", halign='center')
                },
                {
                    'title': "My Account",
                    'icon': "account-circle",
                    'widget': MDLabel(text="My account/profile info", halign='center')
                }
            ]
        )

        root.add_widget(nav_bar)
        return root


if __name__ == '__main__':
    Carrepsa().run()
