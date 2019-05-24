from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, Clock
from kivy.uix.relativelayout import RelativeLayout

from presenter.utils.route import Route

Builder.load_file("view/utils/router.kv")


class Router(RelativeLayout):
    """Takes (Route) children widgets and only displays the Route widget with route=selected_route"""

    selected_route = StringProperty()

    def __init__(self, **kwargs):
        """Initializes the router"""
        super(Router, self).__init__()
        self._routes = dict()
        self.history = []
        Clock.schedule_once(self._init_ui, 0)

    def _init_ui(self, _):
        if self.selected_route is not None:
            self.history.append(self.selected_route)

    def on_selected_route(self, instance, value):
        """Method called when the 'selected_route' property changes value."""
        self.route(value)

    def add_widget(self, route: Route, index=0, canvas=None):
        """Adds a widget to the router, expects a widget of type Route"""
        # This is needed because the path property can't be read
        # until the route widget has been initialized.

        Clock.schedule_once(lambda *_: self._add(route), 0)

    def _add(self, route):
        """Adds the route unless there is a path conflict"""
        if route.path in self._routes:
            raise Exception("Route path must be unique")
        self._routes[route.path] = route
        super(Router, self).add_widget(route)
        if route.path == self.selected_route:
            Clock.schedule_once(lambda *_: self._set_current_route(route.path),
                                0)

    def _set_current_route(self, route_path: str):
        """Set the route that should be displayed"""
        self.clear_widgets()
        if route_path in self._routes:
            route = self._routes[route_path]
            super(Router, self).add_widget(route)
            app = App.get_running_app()
            window = app.root_window
            window.dispatch('on_resize', *window.system_size)


    def route(self, path: str):
        """Change the route of the router"""
        self._set_current_route(path)
        self.history.append(path)

    def go_back(self):
        """Navigate to the previous route"""
        if len(self.history) > 1:
            self.history.pop()
            self._set_current_route(self.history[len(self.history) - 1])
