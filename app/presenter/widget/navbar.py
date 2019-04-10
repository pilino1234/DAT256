from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.button import MDFloatingActionButton
from kivymd.tabs import MDBottomNavigation, MDBottomNavigationItem
from kivymd.theming import ThemeManager


class NavBar(BoxLayout):
    tabs = ListProperty()
    fab_icon = StringProperty('android')
    fab_callback = ObjectProperty(lambda x: None)
    fab_color = ListProperty([1, 0, 0])

    def __init__(self, **kwargs):
        super(NavBar, self).__init__(**kwargs)

        float_layout = FloatLayout()
        self.nav_bar = MDBottomNavigation()
        for tab in self.tabs:
            self.add_tab(**tab)

        self.fab = AppBarActionButton(y=self.nav_bar.height // 2,
                                      x=Window.width // 2 - dp(56) // 2, opacity=1, size=(dp(56), dp(56)),
                                      on_release=self.fab_callback,
                                      action_button_color=self.fab_color,
                                      icon=self.fab_icon)

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


class AppBarActionButton(MDFloatingActionButton):
    action_button_color = ListProperty()
