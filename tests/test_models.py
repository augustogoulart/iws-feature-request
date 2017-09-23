from unittest import TestCase

from feature_request.app import create_app
from feature_request.models import FeatureRequest, Client
from feature_request.models import db, Manager


class TestFeatureRequestResource(TestCase):
    """
    Manager.add() is a wrapper for db.session.add() and db.session.commit()
    db.session.commit() is expected to return None, so Manager.add() is as well

    """

    def setUp(self):
        self.app = create_app('tests.config')
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.client = Client(name='Client A')

        self.feature_request = FeatureRequest(
            title='Feature request',
            description='Description',
            target_date='2017-10-10',
            priority=1,
            product_area='Billing',
            client=self.client
        )
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_manager_add(self):
        self.assertIsNone(Manager.add(self, self.feature_request))

    def test_manager_update(self):
        self.assertIsNone(Manager.update(self.feature_request))
