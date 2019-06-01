from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("view/auth/welcome.kv")


class Welcome(BoxLayout):
    """The welcome view, the first view displayed to unauthenticated users."""

    pass
