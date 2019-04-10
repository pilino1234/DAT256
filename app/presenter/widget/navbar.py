from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.button import MDFloatingActionButton
from kivymd.tabs import MDBottomNavigation, MDBottomNavigationItem
from kivymd.theming import ThemeManager, ThemableBehavior


class NavBar(BoxLayout, ThemableBehavior):
    tabs = ListProperty()
    fab_icon = StringProperty('android')
    fab_callback = ObjectProperty(lambda x: None)
    fab_color = ListProperty([1, .7568627450980392, .027450980392156862, 1])

    def __init__(self, **kwargs):
        super(NavBar, self).__init__(**kwargs)

        float_layout = FloatLayout()
        self.nav_bar = MDBottomNavigation()

        for tab in self.tabs:
            if tab is None:
                self.add_space()
            else:
                self.add_tab(**tab)

        self.fab = MDFloatingActionButton(y=self.nav_bar.height // 2,
                                          x=Window.width // 2 - dp(56) // 2, opacity=1, size=(dp(56), dp(56)),
                                          on_release=self.fab_callback,
                                          icon=self.fab_icon)

        self.fab.md_bg_color = self.fab_color
        self.fab.elevation_normal = 8

        float_layout.add_widget(self.nav_bar)
        float_layout.add_widget(self.fab)
        self.add_widget(float_layout)

        Window.bind(on_resize=self.on_resize)

    def on_resize(self, instance=None, width=None, do_again=True):
        self.fab.x = Window.width // 2 - dp(56) // 2

    def add_tab(self, title: str, icon: str, widget: Widget):
        nav_item = MDBottomNavigationItem(
            text=title,
            icon=icon,
            name=title.lower().replace(" ", "-")
        )
        nav_item.add_widget(widget)
        self.nav_bar.add_widget(nav_item)

    def add_space(self):
        self.nav_bar.add_widget(DummyNavItem())


class DummyNavItem(MDBottomNavigationItem):
    def __init__(self):
        self.icon='dots-horizontal'
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
