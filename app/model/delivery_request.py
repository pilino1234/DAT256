from collections import namedtuple
from enum import IntEnum

from model.location import Location
from model.minified_user import MinifiedUser


class Status(IntEnum):
    """Status codes for delivery requests."""  # noqa: D204
    AVAILABLE = 0
    ACCEPTED = 1
    TRAVELLING = 2
    DELIVERED = 3
    CANCELLED_BY_ASSISTANT = 4


class DeliveryRequest:
    """Represents a request for a delivery of items from point A to B."""

    _weight_prop = namedtuple('_weight_prop', ['icon', 'text'])
    _weight_props = [
        _weight_prop('walk', "Small"),
        _weight_prop('car', "Medium"),
        _weight_prop('truck', "Large")
    ]

    def __init__(self, uid: str, item: str, description: str, origin: dict,
                 destination: dict, reward: int, weight: int, fragile: bool,
                 status: Status, money_lock: int, owner: dict, assistant: dict,
                 image_path: str, **kwargs):
        """Initializes the delivery list"""
        self.uid: str = uid
        self.item: str = item
        self.description: str = description
        self.origin: Location = Location(**origin)
        self.destination: Location = Location(**destination)
        self.reward: int = reward
        self.weight: int = weight
        self.fragile: bool = fragile
        self.status: Status = status
        self.money_lock: int = money_lock

        self.owner: MinifiedUser = MinifiedUser(**owner)

        if assistant:
            self.assistant: MinifiedUser = MinifiedUser(**assistant)
        self.image_path: str = image_path

        self.weight_text = self._weight_props[weight].text
        self.weight_icon = self._weight_props[weight].icon
        self.status_text = self.status.name.title()

    def _to_text(self, status: Status) -> str:
        """Converts status into a pretty text"""
        if status == Status.CANCELLED_BY_ASSISTANT:
            return "Cancelled by assistant"
        else:
            return status.name.title()

    def __str__(self):
        """Format a delivery request for printing"""
        return "Delivery request {uid} | {name}, from: {from_} -> to: {to}, " \
               "reward: {reward}, money_lock: {money_lock}, " \
               "weight: {weight}, fragile: {fragile}, status: {status}, " \
               "description: {description}, image_path: {image_path}".format(
                   uid=self.uid, name=self.item, from_=self.origin,
                   to=self.destination, reward=self.reward,
                   money_lock=self.money_lock, weight=self.weight,
                   fragile=self.fragile, status=self.status,
                   description=self.description, image_path=self.image_path)

    def to_dict(self):
        """
        Convert a DeliveryRequest object to a dict.

        :return: A dict that can be used with third-party software.
        :rtype: dict
        """
        req_dict = {}
        req_dict.update({'uid': self.uid})
        req_dict.update({'item': self.item})
        req_dict.update({'description': self.description})
        req_dict.update({'origin': self.origin.to_dict()})
        req_dict.update({'destination': self.destination.to_dict()})
        req_dict.update({'reward': self.reward})
        req_dict.update({'weight': self.weight})
        req_dict.update({'fragile': self.fragile})
        req_dict.update({'status': self.status.value})
        req_dict.update({'money_lock': self.money_lock})
        req_dict.update({'owner': self.owner.to_dict()})
        req_dict.update({
            'assistant':
            self.assistant.to_dict() if self.has_assistant() else {}
        })
        req_dict.update({'image_path': self.image_path})

        return req_dict

    @property
    def distance_pretty(self) -> str:
        """Computes distance between origin and destination in kilometers"""
        return str(round(self.distance_km, 1)) + " km"

    @property
    def distance_km(self) -> float:
        """Computes distance between origin and destination in kilometres"""
        return self.origin.dist_to(self.destination)

    @property
    def reward_pretty(self) -> str:
        """Pretty formats reward in local currency."""
        return str(self.reward) + " kr"

    def has_assistant(self):
        """Checks if the delivery request has an assistant"""
        return hasattr(self, "assistant")
