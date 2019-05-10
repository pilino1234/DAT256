from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.tabs import MDBottomNavigationItem
from kivymd.theming import ThemableBehavior
from presenter.my_posted_requests import MyPostedRequests
from presenter.user_profile_view import UserProfileView

from kivy.lang import Builder
Builder.load_file("view/navbar.kv")


class NavBarWithFAB(BoxLayout, ThemableBehavior):
    """
    Widget that lets lets the user navigate between different tabs.

    It features a circular Floating Action Button above the center of the bar.
    Supports blank tab slots through BlankNavItem.
    """

    fab_callback = ObjectProperty(lambda: None)
    __tab_loaded = set()  # type: set

    def __init__(self, **kwargs):
        """Initialize the navigation bar"""
        super(NavBarWithFAB, self).__init__(**kwargs)
        self.ids.fab.on_release = self.fab_callback

    def _load_posted_requests(self, tab):
        if tab not in self.__tab_loaded:
            self.__tab_loaded.add(tab)
            tab.add_widget(MyPostedRequests())

    def _load_profile_view(self, tab):
        if tab not in self.__tab_loaded:
            self.__tab_loaded.add(tab)
            tab.add_widget(UserProfileView())


class BlankNavItem(MDBottomNavigationItem):
    """
    Blank navigation tab.

    This approach of getting a blank navigation tab is not ideal, but works for now.
    """

    def on_tab_touch_down(self, *args):  # noqa: D102
        pass

    def on_tab_touch_move(self, *args):  # noqa: D102
        pass

    def on_tab_touch_up(self, *args):  # noqa: D102
        pass

    def on_tab_press(self, *args):  # noqa: D102
        pass

    def on_tab_release(self, *args):  # noqa: D102
        pass
