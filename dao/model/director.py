from marshmallow import Schema, fields
from setup_db import db

class Director(db.Model):
    __tablname__ = "director"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()