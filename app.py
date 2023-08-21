from flask import Flask, request
from flask_restful import Resource
from flask import make_response
from config import api, app, db
from models import Job, Quote, Company
import scraper





class Home(Resource):
    def get(self):
        return make_response("HOWDY")


class Quotes(Resource):
    def get(self):
        quotes = [q.to_dict() for q in Quote.query.all()]
        return make_response(quotes, 200)
    
    def post(self):
        data = request.get_json()
        try:
            newAd = Quote(
                quote=data['quote'], 
                by = data['by']
            )
        except:
            return make_response({"error": "validation error, please try again"}, 400)
        try:
            db.session.add(newAd)
            db.session.commit()
        except:
            return make_response({"error": "validation error, please try again"}, 400)
        
        return make_response(newAd.to_dict(), 201)



    
#custom route for webscraper
@app.route('/scrape')
def getjobs():
    oddball_jobs = scraper.scrapeOddball()
    return make_response(oddball_jobs)
    

api.add_resource(Home, '/')
api.add_resource(Quotes, '/quotes')


if __name__ == '__main__':
    app.run(port=5555, debug=True)