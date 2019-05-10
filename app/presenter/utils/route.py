from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout


class Route(RelativeLayout):
    """
    Child Widget to the Router

    A route is a widget which has a single "path" property.
    It expects a router parent, and the router can navigate
    to the route by specifying the corresponding path.
    """

    path = StringProperty()
