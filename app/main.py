from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.label import MDLabel
from kivymd.theming import ThemeManager

from presenter.widget.navbar import NavBarWithFAB
from presenter.widget.calculator import CalculatorWidget

root = BoxLayout()


class Carrepsa(App):
    theme_cls = ThemeManager(primary_palette="Blue")

    def build(self):
        root.add_widget(self.__nav_bar())
        return root

    def __nav_bar(self):
        return NavBarWithFAB(nav_tabs=[{
            'title':
            "Map",
            'icon':
            "map-marker",
            'widget':
            MDLabel(text="Show the map here", halign='center')
        }, {
            'title':
            "My Packages",
            'icon':
            "package",
            'widget':
            MDLabel(text="List of my packages", halign='center')
        }, None, {
            'title':
            "Deliver",
            'icon':
            "car",
            'widget':
            MDLabel(text="Delivery stuff", halign='center')
        }, {
            'title': "My Account",
            'icon': "account-circle",
            'widget': CalculatorWidget()
        }],
                             fab_icon='package-variant',
                             fab_callback=lambda x: print("FAB pressed!"),
                             fab_color=[0.85, 0.85, 0.85, 1])


if __name__ == '__main__':
    Carrepsa().run()
