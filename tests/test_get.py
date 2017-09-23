from unittest import TestCase
from feature_request.app import create_app
from feature_request.models import db


class TestGet(TestCase):
    def setUp(self):
        self.app = create_app('tests.config')
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_user_name = 'testuser'
        self.test_user_password = 'testuser'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_assert_1_1(self):
        self.assertEqual(1, 1)

