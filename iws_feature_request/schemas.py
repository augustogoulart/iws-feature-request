from models import ma, FeatureRequest, Client
from flask_marshmallow import fields
from marshmallow import fields, pre_load, validate


class ClientSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))
    url = ma.URLFor('api.clientresource', id='<id>', _external=True)

    requests = fields.Nested('FeatureRequestSchema', many=True, exclude=('client',))


class FeatureRequestSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    target_date = fields.String(required=True)
    client = fields.Nested(ClientSchema, only=['id', 'name'], required=True)

    @pre_load
    def process_client(self, data):
        client = data.get('client')
        if client:
            if isinstance(client, dict):
                client_name = client.get('name')
            else:
                client_name = client
            client_dict = dict(name=client_name)

        else:
            client_dict = {}

        data['client'] = client_dict
        return data

