from config import db
from sqlalchemy_serializer import SerializerMixin


class Job(db.Model, SerializerMixin):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    company = db.Column(db.String)

class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key = True)
    quote = db.Column(db.String, nullable = False)
    by = db.Column(db.String, nullable = False)

    