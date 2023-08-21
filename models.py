from config import db
from sqlalchemy_serializer import SerializerMixin



class Company(db.Model, SerializerMixin):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)


class Job(db.Model, SerializerMixin):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key = True)
    quote = db.Column(db.String, nullable = False)
    by = db.Column(db.String, nullable = False)

    