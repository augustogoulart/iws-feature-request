from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


class Manager:
    def get(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.remove(resource)
        return db.session.commit()


class FeatureRequest(db.Model, Manager):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='CASCADE'), nullable=False)
    client = db.relationship('Client', backref=db.backref('messages', order_by='FeatureRequest.title'))
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, title, description, target_date):
        self.title = title
        self.description = description
        self.target_date = target_date


class Client(db.Model, Manager):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


class ProductArea(db.Model, Manager):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name
