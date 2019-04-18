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

    _status_types = ["available", "accepted", "travelling", "delivered"]

    def __init__(self, item: str, origin: str, destination: str, reward: int,
                 weight: int, fragile: bool, status: int, money_lock: int):
        """Initializes the delivery list"""
        self.item = item
        self.origin = origin
        self.destination = destination
        self.reward = reward
        self.weight = weight
        self.fragile = fragile
        self.status = status
        self.money_lock = money_lock

        self.weight_text = self._weight_props[weight].text
        self.weight_icon = self._weight_props[weight].icon
        self.status_text = self._status_types[status]

    def get_distance_pretty(self) -> str:
        """Computes distance between origin and destination in kilo meters"""
        return "7 km"

    def get_reward_pretty(self) -> str:
        """Pretty formats reward in local currency."""
        return str(self.reward) + " kr"
