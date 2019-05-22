import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_getter import DeliveryRequestGetter
from model.location import Location
from model.minified_user import MinifiedUser


class RequestGetterTest(unittest.TestCase):
    def test_query(self):
        delivery_requests = DeliveryRequestGetter.query(
            u'owner.uid', u'==', u'94MTAsYEcpTBGW98MQbjyuGEPUx1')

        self.assertEqual(
            len(delivery_requests), 1, msg="Expected only 1 match.")

        expected = DeliveryRequest(
            uid='DLpVc0QmbOHzfDo24Hpp',
            item='Xbox controller',
            description='I AM USED FOR TESTS. DO NOT REMOVE',
            origin=Location("Odenvägen 1, SE-194 63 Odenslunda, Sweden",
                            59.51224, 17.93536).to_dict(),
            destination=Location("Rolsmo 1, SE-360 24 Linneryd, Sweden",
                                 56.64989, 15.16624).to_dict(),
            reward=123,
            weight=0,
            fragile=False,
            status=Status.AVAILABLE,
            money_lock=23,
            owner=MinifiedUser("", "", "",
                               "94MTAsYEcpTBGW98MQbjyuGEPUx1").to_dict(),
            assistant=MinifiedUser("", "", "", "").to_dict(),
            image_path='')

        self.assertDictEqual(delivery_requests[0].to_dict(),
                             expected.to_dict())

    def test_get_by_id(self):
        delivery_request = DeliveryRequestGetter.get_by_id(
            u'DLpVc0QmbOHzfDo24Hpp')

        expected = DeliveryRequest(
            uid='DLpVc0QmbOHzfDo24Hpp',
            item='Xbox controller',
            description='I AM USED FOR TESTS. DO NOT REMOVE',
            origin=Location("Odenvägen 1, SE-194 63 Odenslunda, Sweden",
                            59.51224, 17.93536).to_dict(),
            destination=Location("Rolsmo 1, SE-360 24 Linneryd, Sweden",
                                 56.64989, 15.16624).to_dict(),
            reward=123,
            weight=0,
            fragile=False,
            status=Status.AVAILABLE,
            money_lock=23,
            owner=MinifiedUser("", "", "",
                               "94MTAsYEcpTBGW98MQbjyuGEPUx1").to_dict(),
            assistant=MinifiedUser("", "", "", "").to_dict(),
            image_path='')

        self.assertDictEqual(delivery_request.to_dict(), expected.to_dict())
