from collections import namedtuple
from enum import IntEnum


class Status(IntEnum):
    """Status codes for delivery requests."""  # noqa: D204
    AVAILABLE = 0
    ACCEPTED = 1
    TRAVELLING = 2
    DELIVERED = 3


class DeliveryRequest:
    """Represents a request for a delivery of items from point A to B."""

    _weight_prop = namedtuple('_weight_prop', ['icon', 'text'])
    _weight_props = [
        _weight_prop('walk', "Small"),
        _weight_prop('bike', "Medium"),
        _weight_prop('car', "Large"),
        _weight_prop('truck', "Huge")
    ]

    def __init__(self, item: str, description: str, origin: str,
                 destination: str, reward: int, weight: int, fragile: bool,
                 status: Status, money_lock: int, owner: str, assistant: str):
        """Initializes the delivery list"""
        self.item = item
        self.description = description
        self.origin = origin
        self.destination = destination
        self.reward = reward
        self.weight = weight
        self.fragile = fragile
        self.status = status
        self.money_lock = money_lock
        self.owner = owner
        self.assistant = assistant

        self.weight_text = self._weight_props[weight].text
        self.weight_icon = self._weight_props[weight].icon
        self.status_text = self.status.name.title()

    def __str__(self):
        """Format a delivery request for printing"""
        return "Delivery request {name}, from: {from_} -> to: {to}, " \
               "reward: {reward}, money_lock: {money_lock}, " \
               "weight: {weight}, fragile: {fragile}, status: {status}, " \
               "desc: {description}".format(name=self.item, from_=self.origin, to=self.destination,
                                            reward=self.reward, money_lock=self.money_lock,
                                            weight=self.weight, fragile=self.fragile,
                                            status=self.status, description=self.description)

    @property
    def distance_pretty(self) -> str:
        """Computes distance between origin and destination in kilometers"""
        return "7 km"

    @property
    def reward_pretty(self) -> str:
        """Pretty formats reward in local currency."""
        return str(self.reward) + " kr"
