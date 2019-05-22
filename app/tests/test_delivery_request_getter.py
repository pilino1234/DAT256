import unittest

from model.delivery_request import DeliveryRequest, Status
from model.delivery_request_getter import DeliveryRequestGetter
from model.firebase.firestore import Firestore
from model.location import Location
from model.minified_user import MinifiedUser
from model.user_getter import UserGetter


class RequestGetterTest(unittest.TestCase):
    def test_query(self):
        user = UserGetter.get_by_id('94MTAsYEcpTBGW98MQbjyuGEPUx1')
        delivery_requests = DeliveryRequestGetter.query(
            u'owner.uid', u'==', u'94MTAsYEcpTBGW98MQbjyuGEPUx1')

        self.assertGreaterEqual(len(delivery_requests),
                                1,
                                msg="Expected at least 1 match.")

        # Clean up DRs
        for dr in delivery_requests:
            if not dr.uid == 'DLpVc0QmbOHzfDo24Hpp':
                with Firestore.batch('packages') as batch:
                    batch.delete(dr.uid)

        delivery_requests = DeliveryRequestGetter.query(
            u'owner.uid', u'==', u'94MTAsYEcpTBGW98MQbjyuGEPUx1')

        self.assertEqual(len(delivery_requests), 1, msg="Expected 1 match.")

        expected = DeliveryRequest(
            uid='DLpVc0QmbOHzfDo24Hpp',
            item='Xbox controller',
            description='I AM USED FOR TESTS. DO NOT REMOVE',
            origin=Location("Odenvägen 1, SE-194 63 Odenslunda, Sweden",
                            latitude=59.51224,
                            longitude=17.93536).to_dict(),
            destination=Location("Rolsmo 1, SE-360 24 Linneryd, Sweden",
                                 latitude=56.64989,
                                 longitude=15.16624).to_dict(),
            reward=123,
            weight=0,
            fragile=False,
            status=Status.AVAILABLE,
            money_lock=23,
            owner=user.to_minified().to_dict(),
            assistant=dict(),
            image_path='')
        self.assertDictEqual.__self__.maxDiff = None
        self.assertDictEqual(delivery_requests[0].to_dict(),
                             expected.to_dict())

    def test_get_by_id(self):
        delivery_request = DeliveryRequestGetter.get_by_id(
            u'DLpVc0QmbOHzfDo24Hpp')

        expected = DeliveryRequest(
            uid='DLpVc0QmbOHzfDo24Hpp',
            item='Xbox controller',
            description='I AM USED FOR TESTS. DO NOT REMOVE',
            origin=Location(name="Odenvägen 1, SE-194 63 Odenslunda, Sweden",
                            latitude=59.51224,
                            longitude=17.93536).to_dict(),
            destination=Location(name="Rolsmo 1, SE-360 24 Linneryd, Sweden",
                                 latitude=56.64989,
                                 longitude=15.16624).to_dict(),
            reward=123,
            weight=0,
            fragile=False,
            status=Status.AVAILABLE,
            money_lock=23,
            owner=MinifiedUser(
                mail="travis@carrepsa.ci",
                name=
                'Travis CI Account - DON\'T DELETE OR YOULL BREAK THE ENTIRE CI WORKFLOW/UNITTESTS REEEEEEEEEEEEEEEEEEEEEEEE',
                phonenumber='-inf',
                uid="94MTAsYEcpTBGW98MQbjyuGEPUx1").to_dict(),
            assistant=dict(),
            image_path='')

        self.assertDictEqual.__self__.maxDiff = None
        self.assertDictEqual(delivery_request.to_dict(), expected.to_dict())
