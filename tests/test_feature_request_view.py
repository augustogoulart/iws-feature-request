from unittest import TestCase

from flask import url_for, json

from feature_request.app import create_app
from feature_request.models import FeatureRequest, Client
from feature_request.models import db


class TestFeatureRequestResource(TestCase):
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

    def test_feature_request_resource_list_get(self):
        resp = self.app_client.get(f"/api/requests/")
        self.assertEqual(200, resp.status_code)

    def test_feature_request_get_response(self):
        resp = self.app_client.get(f"/api/requests/{self.feature_request.id}")
        contents = ['id', 'title', 'description', 'target_date', 'priority', 'product_area', 'client']
        for content in contents:
            with self.subTest():
                self.assertIn(content, str(resp.data))

    def test_feature_request_can_delete(self):
        resp = self.app_client.delete(f"/api/requests/{self.feature_request.id}")
        self.assertEqual(204, resp.status_code)

    def test_feature_request_post_success(self):
        url = url_for('api.featurerequestresourcelist', _external=True)

        data = {'title': 'title', 'description': 'description', 'client': 'client', 'priority': 1,
                'target_date': '2017-10-10', 'product_area': 'product_area'}

        response = self.app_client.post(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data))
        self.assertEqual(201, response.status_code)

    def test_feature_request_post_erros(self):
        url = url_for('api.featurerequestresourcelist', _external=True, )

        data = {}

        response = self.app_client.post(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data))
        self.assertEqual(400, response.status_code)

    def test_feature_request_patch_succes(self):
        url = url_for('api.featurerequestresource', _external=True, id=1)

        data = {'title': 'title', 'description': 'description', 'client': 'client', 'priority': 1,
                'target_date': '2017-10-10', 'product_area': 'product_area'}

        response = self.app_client.patch(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data))

        self.assertEqual(200, response.status_code)

    def test_feature_request_patch_errors(self):
        url = url_for('api.featurerequestresource', _external=True, id=1)

        data = {}

        response = self.app_client.patch(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data))

        self.assertEqual(400, response.status_code)

    def test_feature_request_patch_empty(self):
        url = url_for('api.featurerequestresource', _external=True, id=1)

        data = {'title': 'I forgot the other fields'}

        response = self.app_client.patch(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data))

        self.assertEqual(400, response.status_code)

    def test_feature_request_query_error(self):
        url = url_for('api.featurerequestresource', _external=True, id=1)

        data = {}
        self.client = None

        response = self.app_client.patch(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(data))

        self.assertEqual(400, response.status_code)

    def test_feature_request_priority_updating_on_new_request(self):
        url = url_for('api.featurerequestresourcelist', _external=True)

        previous = {'title': 'title', 'description': 'description', 'client': 'client', 'priority': 1,
                    'target_date': '2017-10-10', 'product_area': 'product_area'}

        self.app_client.post(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(previous))

        previous_resp = self.app_client.get("/api/requests/")

        updated = {'title': 'title', 'description': 'description', 'client': 'client', 'priority': 1,
                   'target_date': '2017-10-10', 'product_area': 'product_area'}

        self.app_client.post(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(updated))

        updated_resp = self.app_client.get("/api/requests/")
        self.assertNotEqual(previous_resp, updated_resp)

    def test_feature_request_priority_updating_on_delete(self):
        url = url_for('api.featurerequestresourcelist', _external=True)

        new_request = {'title': 'title', 'description': 'description', 'client': 'client', 'priority': 1,
                       'target_date': '2017-10-10', 'product_area': 'product_area'}

        self.app_client.post(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(new_request))

        previous_resp = self.app_client.get("/api/requests/2")
        self.app_client.delete(f"/api/requests/{self.feature_request.id}")

        updated_resp = self.app_client.get("/api/requests/2")
        self.assertNotEqual(previous_resp, updated_resp)

    def test_feature_request_priority_updating_on_update(self):
        url = url_for('api.featurerequestresourcelist', _external=True)

        new_request = {'title': 'title', 'description': 'description', 'client': 'Client A', 'priority': 2,
                       'target_date': '2017-10-10', 'product_area': 'product_area'}

        self.app_client.post(
            url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps(new_request))

        previous_resp = self.app_client.get("/api/requests/2")

        delete_url = url_for('api.featurerequestresource', _external=True, id=1)

        self.app_client.delete(
            delete_url,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        updated_resp = self.app_client.get("/api/requests/2")

        self.assertNotEqual(previous_resp, updated_resp)
