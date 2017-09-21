from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError

from models import db, FeatureRequest, Client
from schemas import FeatureRequestSchema, ClientSchema

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
        try:
            feature_request.delete(feature_request)
            return '', 204

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = str(e)
            return resp, 401


class FeatureRequestResourceList(Resource):
    def get(self):
        query = FeatureRequest.query.all()
        return feature_request_schema.dump(query, many=True).data

    def post(self):
        request_dict = request.get_json()

        if not request_dict:
            return {'message': 'No input data provided'}, 400

        errors = feature_request_schema.validate(request_dict)

        if errors:
            return errors, 400

        try:
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
                client=client
            )
            feature_request.add(feature_request)

            query = FeatureRequest.query.get(feature_request.id)

            return feature_request_schema.dump(query).data, 201

        except SQLAlchemyError as error:
            db.session.rollback()
            return str(error), 400


class ClientResource(Resource):
    def get(self, id):
        client = Client.query.get_or_404(id)
        return client_schema.dump(client).data


class ClientListResource(Resource):
    def get(self):
        client = Client.query.all()
        return client_schema.dump(client, many=True).data

    def post(self):
        context = request.get_json()
        if not context:
            return {'message': 'No input data provided'}, 400

        errors = client_schema.validate(context)

        if errors:
            return errors, 400

        try:
            client = Client(context['name'])
            client.add(client)
            query = Client.query.get(client.id)
            return client_schema.dump(query).data, 201
        except SQLAlchemyError as error:
            db.session.rollback()
            return str(error), 400


class FeaturesByClientesResource(Resource):
    def get(self, id):
        query = FeatureRequest.query.filter_by(client_id=id)
        return feature_request_schema.dump(query, many=True).data


api.add_resource(FeatureRequestResourceList, '/requests/')
api.add_resource(FeatureRequestResource, '/requests/<int:id>')

api.add_resource(ClientListResource, '/clients/')
api.add_resource(ClientResource, '/clients/<int:id>')

api.add_resource(FeaturesByClientesResource, '/clients/<int:id>/requests')
