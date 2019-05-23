import functools
import os
import threading
import unittest

from model.delivery_request import Status
from model.delivery_request_uploader import DeliveryRequestUploader
from model.firebase.auth import Auth
from model.firebase.firestore import Firestore
from tests.utils import create_delivery_request


class FirestoreTest(unittest.TestCase):
    def setUp(self) -> None:
        mail = os.environ['CARREPSA_CI_EMAIL']
        password = os.environ['CARREPSA_CI_PASS']

        Auth.sign_in(mail, password)

    def test_subscription(self):
        event = threading.Event()

        callback_with_event = functools.partial(lambda *_: event.set(), event)
        Firestore.subscribe("packages", callback_with_event)

        request = create_delivery_request()
        self.assertIsNotNone(request)
        DeliveryRequestUploader.upload(request)

        event.wait()

        self.assertTrue(event.is_set())

        Firestore.unsubscribe("packages")

        Firestore.unsubscribe("some_invalid_thing_to_unsubscribe_from")

    def test_get_packages(self):
        delivery_requests = Firestore.get("packages")
        for delivery_request in delivery_requests:
            self.assertIsNotNone(delivery_request.get("item"))

    def test_batching(self):
        delivery_request = create_delivery_request()

        with Firestore.batch('packages') as batch:
            dr_dict = delivery_request.to_dict()
            uid = batch.create_with_random_id(dr_dict)
            batch.update(uid, {
                'status': Status.ACCEPTED,
                'assistant': 'pIAeLAvHXp0KZKWDzTMz'
            })
            batch.set(uid, dr_dict)

        self.assertTrue(
            any(request.to_dict()['uid'] == "TEST"
                for request in Firestore.get('packages')))

        with Firestore.batch('packages') as batch:
            batch.delete(uid)

    def test_batch_exception(self):
        with self.assertRaises(TypeError), Firestore.batch(
                'packages') as batch:
            batch.delete(1524)
