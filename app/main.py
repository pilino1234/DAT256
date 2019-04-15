from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager

from presenter.navbar import NavBarWithFAB


class Carrepsa(App):
    theme_cls = ThemeManager(primary_palette="Blue")

    def build(self):
        root = BoxLayout()
        root.add_widget(
            NavBarWithFAB(fab_callback=lambda: print("FAB pressed!")))
        return root


if __name__ == '__main__':
    Carrepsa().run()
