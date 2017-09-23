from unittest import TestCase

from feature_request.app import create_app


class TestFeatureRequestResource(TestCase):
    def setUp(self):
        self.app = create_app('tests.config')
        self.app_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_root_url_status_code(self):
        resp = self.app_client.get('/')
        self.assertEqual(200, resp.status_code)

