from flask import Flask
from flask_restful import Resource
from flask import make_response
from config import api, app, db
from models import Job, Quote




class Home(Resource):
    def get(self):
        return make_response("HOWDY")


class Quotes(Resource):
    def get(self):
        quotes = [q.to_dict() for q in Quote.query.all()]
        return make_response(quotes, 200)

    
#custom route for webscraper
@app.route('/scrape')
def getjobs():
    return make_response("web scraper here")
    

api.add_resource(Home, '/')
api.add_resource(Quotes, '/quotes')


if __name__ == '__main__':
    app.run(port=5555, debug=True)