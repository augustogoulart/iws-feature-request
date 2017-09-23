from unittest import TestCase

from feature_request.app import create_app
from feature_request.models import db, Client, FeatureRequest
from feature_request.schemas import FeatureRequestSchema


class TestFeatureRequestSchema(TestCase):
    def setUp(self):
        self.app = create_app('tests.config')
        self.app_client = self.app.test_client()
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
        db.session.add(self.client)
        db.session.add(self.feature_request)
        self.feature_request = FeatureRequest.query.first()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_context_has_client(self):
        data = FeatureRequestSchema().dump(self.feature_request).data
        self.assertIsInstance(FeatureRequestSchema().process_client(data), dict)

    def test_context_has_no_client(self):
        data = {}
        self.assertIsInstance(FeatureRequestSchema().process_client(data), dict)

    def test_context_dict_key(self):
        data = {'client': 'Clietn A'}
        self.assertIsInstance(FeatureRequestSchema().process_client(data), dict)


























