from flask import Blueprint, request
from flask_restful import Api, Resource

from .models import db, FeatureRequest, Client
from .schemas import FeatureRequestSchema, ClientSchema

api_bp = Blueprint('api', __name__)

client_schema = ClientSchema()
feature_request_schema = FeatureRequestSchema()

api = Api(api_bp)


class FeatureRequestResource(Resource):
    def get(self, id):
        feature_request = FeatureRequest.query.get_or_404(id)
        return feature_request_schema.dump(feature_request).data

    def delete(self, id):
        feature_request = FeatureRequest.query.get_or_404(id)
        feature_request.delete(feature_request)
        return 'NO CONTENT', 204

    def patch(self, id):
        feature_request = FeatureRequest.query.get_or_404(id)

        feature_request_dict = request.get_json()

        if not feature_request_dict:
            resp = {'message': 'No input data provided'}
            return resp, 400

        errors = feature_request_schema.validate(feature_request_dict)

        if errors:
            return errors, 400

        client_name = feature_request_dict['client']['name']
        client = Client.query.filter_by(name=client_name).first()
        if client is None:
            client = Client(name=client_name)
            db.session.add(client)
            feature_request.client = client

        feature_request.title = feature_request_dict.get('title')
        feature_request.description = feature_request_dict.get('description')
        feature_request.priority = feature_request_dict.get('priority')
        feature_request.product_area = feature_request_dict.get('product_area')
        feature_request.target_date = feature_request_dict.get('target_date')
        feature_request.update()

        return self.get(id)


class FeatureRequestResourceList(Resource):
    def get(self):
        query = FeatureRequest.query.order_by(FeatureRequest.priority)
        return feature_request_schema.dump(query, many=True).data

    def post(self):
        request_dict = request.get_json()

        errors = feature_request_schema.validate(request_dict)

        if errors:
            return errors, 400

        client_name = request_dict['client']['name']
        client = Client.query.filter_by(name=client_name).first()

        if client is None:
            client = Client(name=client_name)
            db.session.add(client)

        feature_request = FeatureRequest(
            title=request_dict['title'],
            description=request_dict['description'],
            target_date=request_dict['target_date'],
            priority=request_dict['priority'],
            product_area=request_dict['product_area'],
            client=client
        )

        # Check priority before persist

        requests_by_client = FeatureRequest.query.filter_by(client_id=client.id)
        data = feature_request_schema.dump(requests_by_client, many=True).data

        for previous_request in data:
            if previous_request.get('priority') >= int(feature_request.priority):
                update_query = FeatureRequest.query.get_or_404(previous_request.get('id'))
                update_query.priority += 1
                update_query.update()

        feature_request.add(feature_request)

        query = FeatureRequest.query.get(feature_request.id)

        return feature_request_schema.dump(query).data, 201


api.add_resource(FeatureRequestResourceList, '/requests/')
api.add_resource(FeatureRequestResource, '/requests/<int:id>')
