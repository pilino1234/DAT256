from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.button import MDFloatingActionButton
from kivymd.tabs import MDBottomNavigation, MDBottomNavigationItem
from kivymd.theming import ThemeManager, ThemableBehavior

from kivy.lang import Builder
Builder.load_file("view/navbar.kv")


class NavBarWithFAB(BoxLayout, ThemableBehavior):
    '''
    Widget that lets lets the user navigate between different tabs.
    It features a circular Floating Action Button above the center of the bar.
    Supports blank tab slots through BlankNavItem.
    '''

    fab_callback = ObjectProperty(lambda: None)

    def __init__(self, **kwargs):
        super(NavBarWithFAB, self).__init__(**kwargs)
        self.navbar = self.ids.navbar
        self.fab = self.ids.fab

        self.fab.on_release = self.fab_callback


class BlankNavItem(MDBottomNavigationItem):
    '''
    Blank navigation tab.
    This approach of getting a blank navigation tab is not ideal, but works for now.
    '''

    def on_tab_touch_down(self, *args):
        pass

    def on_tab_touch_move(self, *args):
        pass

    def on_tab_touch_up(self, *args):
        pass

    def on_tab_press(self, *args):
        pass

    def on_tab_release(self, *args):
        pass
