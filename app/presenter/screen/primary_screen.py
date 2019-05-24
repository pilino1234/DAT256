from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/screens/primary_screen.kv")


class PrimaryScreen(Screen):
    """
    The primary screen of the app.

    Contains everything except authentication.
    """

    def go_to_request_delivery(self):
        """Opens the main view and navvigates to the 'request-delivery' tab"""
        self.ids.router.route("main")
        Clock.schedule_once(self._open_my_packages_tab, 0)
        self.ids.sp.show()

    def _open_my_packages_tab(self, *_):
        navbar_with_fab = self.ids.navbar
        my_packages_btn = navbar_with_fab.ids.my_packages_btn
        navbar_with_fab._load_posted_requests(my_packages_btn)
        Clock.schedule_once(lambda *_: my_packages_btn.on_tab_press(), 0)

    def go_to_make_delivery(self):
        """Opens the main view and navigates to the 'search' tab"""
        self.ids.router.route("main")
