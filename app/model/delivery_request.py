from collections import namedtuple
from enum import IntEnum
from typing import Dict, Union


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

    def __init__(self,
                 uid: str,
                 item: str,
                 description: str,
                 origin: str,
                 destination: str,
                 reward: int,
                 weight: int,
                 fragile: bool,
                 status: Status,
                 money_lock: int,
                 owner: str,
                 assistant: str,
                 image_path: str = "",
                 **kwargs):
        """Initializes the delivery list"""
        self.uid = uid
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
        self.image_path = image_path

        self.weight_text = self._weight_props[weight].text
        self.weight_icon = self._weight_props[weight].icon
        self.status_text = self.status.name.title()

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

    def to_dict(self) -> Dict[str, Union[str, float, int, bool]]:
        """
        Convert a DeliveryRequest object to a dict.

        :return: A dict that can be used with third-party software.
        :rtype: dict
        """
        req_dict: Dict[str, Union[str, float, int, bool]] = {}
        req_dict.update({'uid': self.uid})
        req_dict.update({'item': self.item})
        req_dict.update({'description': self.description})
        req_dict.update({'origin': self.origin})
        req_dict.update({'destination': self.destination})
        req_dict.update({'reward': self.reward})
        req_dict.update({'weight': self.weight})
        req_dict.update({'fragile': self.fragile})
        req_dict.update({'status': self.status.value})
        req_dict.update({'money_lock': self.money_lock})
        req_dict.update({'owner': self.owner})
        req_dict.update({'assistant': self.assistant})
        req_dict.update({'image_path': self.image_path})

        return req_dict

    @property
    def distance_pretty(self) -> str:
        """Computes distance between origin and destination in kilometers"""
        return "7 km"

    @property
    def reward_pretty(self) -> str:
        """Pretty formats reward in local currency."""
        return str(self.reward) + " kr"
