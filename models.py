from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates



class Company(db.Model, SerializerMixin):
    __tablename__ = 'companies'

    serialize_rules = ('-jobs',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    jobs = db.relationship('Job', backref='company')


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

class ToDo(db.Model, SerializerMixin):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False )
    done = db.Column(db.Boolean,)
    prio = db.Column(db.String)
    
    @validates('prio')
    def validate_prio(self, key, input):
        validCategories = ['TODAY', 'THIS WEEK', 'THIS MONTH', 'THIS YEAR']
        if input not in validCategories:
            raise ValueError("Prio is not valid, choose another selection.")
        return input


# do i need a user model? only if this was going to be for multiple people....

    