from flask import Flask
from flask_restful import Resource, Api
from flask import make_response
from config import api, app, db





class Home(Resource):
    def get(self):
        return make_response("HOWDY")
    
#custom route for webscraper
@app.route('/scrape')
def getjobs():
    return make_response("web scraper here")
    

api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5555, debug=True)