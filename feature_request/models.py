from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


class Manager:
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class FeatureRequest(db.Model, Manager):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_date = db.Column(db.String, nullable=False)
    product_area = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False, default=0)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE'),
                          nullable=False, server_default='0')
    client = db.relationship('Client')

    def __init__(self, title, description, target_date, client, priority, product_area):
        self.title = title
        self.description = description
        self.target_date = target_date
        self.client = client
        self.priority = priority
        self.product_area = product_area


class Client(db.Model, Manager):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name
