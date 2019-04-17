from collections import namedtuple


class DeliveryRequest():
    """Represents a request for a delivery of items from point A to B."""

    _weight_prop = namedtuple('_weight_prop', ['icon', 'text'])
    _weight_props = [
        _weight_prop('walk', "Small"),
        _weight_prop('bike', "Medium"),
        _weight_prop('car', "Large"),
        _weight_prop('truck', "Huge")
    ]

    def __init__(self, origin: str, destination: str, reward: int,
                 weight: int):
        """Initializes the delivery list"""
        self.origin = origin
        self.destination = destination
        self.reward = reward
        self.weight = weight

        self.weight_text = self._weight_props[weight].text
        self.weight_icon = self._weight_props[weight].icon

    def get_distance_pretty(self):
        """Computes distance between origin and destination in kilo meters"""
        return "7 km"