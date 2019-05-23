from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/screens/primary_screen.kv")


class PrimaryScreen(Screen):
    """
    The primary screen of the app.

    Contains everything except authentication.
    """

    def go_to_request_delivery(self):
        self.ids.router.route("main")
        navbar = self.ids.navbar
        navbar.ids.my_delieries_btn.on_tab_press()
        self.ids.sp.show()

    def go_to_make_delivery(self):
        self.ids.router.route("main")

