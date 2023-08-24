from models import Job, Quote, Company, ToDo
from config import db, app


def seed():

    print("deleting previous tables")
    Job.query.delete()
    Quote.query.delete()
    Company.query.delete()
    ToDo.query.delete()

    print("creating new tables")
    db.create_all()

    q1 = Quote(quote="Quality > Quantity. Submit quality application where with each one, you're making personal connections", by='Laura')
    q2 = Quote(quote='You can do this', by='Kimmy')
    q3 = Quote(quote="Don't slow down. Keep grinding.", by="April")
    q4 = Quote(quote="Make sure you havea good commit history. Write out informative commit messages", by="David")
    q5 = Quote(quote="Don't take rejection personally, and keep those emotions under wraps - be stoic. If you let it get to you, it will take you a while to get back on the horse", by="Gehrig")
    q6 = Quote(quote="Learn how to test your own code. Start with unit testing", by="April")
    q7 = Quote(quote="Don't stop grinding your data structures and algos. This is how you'll pass interviews", by="Megan")

    c1 = Company(name="Oddball")
    c2 = Company(name="Mindex")

    t1 = ToDo(title="add live clock", done=False)

    
    db.session.add_all([q1, q2, q3, q4, q5, q6, q7, c1, c2, t1])
    db.session.commit() 

    print("done seeding!")




if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        seed()





    




