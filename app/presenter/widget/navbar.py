from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.button import MDFloatingActionButton
from kivymd.tabs import MDBottomNavigation, MDBottomNavigationItem
from kivymd.theming import ThemeManager, ThemableBehavior


class NavBarWithFAB(BoxLayout, ThemableBehavior):
    '''
    Widget that lets lets the user navigate between different tabs.
    It features a circular Floating Action Button above the center of the bar.
    Supports blank tab slots through BlankNavItem.
    '''

    nav_tabs = ListProperty()
    fab_icon = StringProperty('android')
    fab_callback = ObjectProperty(lambda x: None)
    fab_color = ListProperty([1, .7568627450980392, .027450980392156862, 1])
    fab_diameter = 64

    def __init__(self, **kwargs):
        super(NavBarWithFAB, self).__init__(**kwargs)

        self.__init_navbar()
        self.__init_fab()

        float_layout = FloatLayout()
        float_layout.add_widget(self.navbar)
        float_layout.add_widget(self.fab)
        self.add_widget(float_layout)

        Window.bind(on_resize=self._on_resize)

    def __init_navbar(self):
        self.navbar = MDBottomNavigation()

        for tab in self.nav_tabs:
            if tab is None:
                self.__add_space()
            else:
                self.__add_tab(**tab)

    def __init_fab(self):
        x = self.navbar.height // 2
        y = self.navbar.width // 2 - dp(self.fab_diameter) // 2
        self.fab = MDFloatingActionButton(x=x,
                                          y=y,
                                          on_release=self.fab_callback,
                                          icon=self.fab_icon)

        self.fab.md_bg_color = self.fab_color
        self.fab.elevation_normal = 8

    def __add_tab(self, title: str, icon: str, widget: Widget):
        nav_item = MDBottomNavigationItem(text=title,
                                          icon=icon,
                                          name=title.lower().replace(" ", "-"))
        nav_item.add_widget(widget)
        self.navbar.add_widget(nav_item)

    def __add_space(self):
        self.navbar.add_widget(BlankNavItem())

    def _on_resize(self, instance=None, width=None, do_again=True):
        self.fab.x = Window.width // 2 - dp(self.fab_diameter) // 2
        self.fab.size = (dp(self.fab_diameter), dp(self.fab_diameter))


class BlankNavItem(MDBottomNavigationItem):
    '''
    Blank navigation tab.
    This approach of getting a blank navigation tab is not ideal, but works for now.
    '''

    def __init__(self):
        self.icon = 'dots-horizontal'
        pass

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
