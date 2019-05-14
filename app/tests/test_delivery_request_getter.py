import os
import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_getter import DeliveryRequestGetter


class RequestGetterTest(unittest.TestCase):
    def test_query(self):
        delivery_requests = DeliveryRequestGetter.query(
            u'owner', u'==', u'test_owner')

        self.assertEqual(len(delivery_requests),
                         1,
                         msg="Expected only 1 match.")

        expected = DeliveryRequest(uid='mByJp1N4OqFesOL5Xd9R',
                                   item='test1',
                                   description='test4',
                                   origin='test2',
                                   destination='test3',
                                   reward=1,
                                   weight=2,
                                   fragile=False,
                                   status=Status.ACCEPTED,
                                   money_lock=2,
                                   owner='test_owner',
                                   assistant='pIAeLAvHXp0KZKWDzTMz')

        self.assertDictEqual(delivery_requests[0].to_dict(),
                             expected.to_dict())

    def test_get_by_id(self):
        delivery_request = DeliveryRequestGetter.get_by_id(
            u'mByJp1N4OqFesOL5Xd9R')

        expected = DeliveryRequest(uid='mByJp1N4OqFesOL5Xd9R',
                                   item='test1',
                                   description='test4',
                                   origin='test2',
                                   destination='test3',
                                   reward=1,
                                   weight=2,
                                   fragile=False,
                                   status=Status.ACCEPTED,
                                   money_lock=2,
                                   owner='test_owner',
                                   assistant='pIAeLAvHXp0KZKWDzTMz')

        self.assertDictEqual(delivery_request.to_dict(), expected.to_dict())
