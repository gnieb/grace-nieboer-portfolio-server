from models import Job, Quote
from config import db, app


def seed():

    print("deleting tables")
    Job.query.delete()
    Quote.query.delete()

    print("creating tables")
    db.create_all()

    q1 = Quote(quote='Lorem Ipsum', by='unknown')
    q2 = Quote(quote='You can do this', by='Kimmy')
    
    db.session.add_all([q1, q2])
    db.session.commit() 

    print("done seeding!")




if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        seed()





    




