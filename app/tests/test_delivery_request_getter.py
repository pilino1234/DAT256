import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_getter import DeliveryRequestGetter


class RequestGetterTest(unittest.TestCase):
    def test_query(self):
        delivery_requests = DeliveryRequestGetter.query(
            u'owner', u'==', u'test_owner')

        self.assertDictEqual(
            request_dict,
            expected,
            msg="The converted dict should equal the expected dict. "
            "You may want to check the data definition in the team "
            "GDrive to confirm all data is present and correct.")

    def test_get_by_id(self):
        delivery_request = DeliveryRequestGetter.get_by_id(
            u'mByJp1N4OqFesOL5Xd9R')

        expected = DeliveryRequest(description='test4',
                                   destination='test3',
                                   fragile=False,
                                   item='test1',
                                   money_lock=1,
                                   origin='test2',
                                   reward=1,
                                   status=0,
                                   weight=2)

        self.assertDictEqual(request_dict,
                             expected,
                             msg="Should fetch correct delivery.")
