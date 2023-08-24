from flask import Flask, request
from flask_restful import Resource
from flask import make_response
from config import api, app, db
from models import Job, Quote, Company, ToDo
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

class ToDos(Resource):
    def get(self):
        tasks = [t.to_dict() for t in ToDo.query.all()]
        return make_response(tasks, 200)
    
class ToDoById(Resource):
    def get(self, id):
        task = ToDo.query.filter_by(id=id).first()
        if not task:
            return make_response({"error":"ToDo Not Found!"}, 404)
        return make_response(task.to_dict(), 200)


    def patch(self, id):
        task = ToDo.query.filter_by(id = id).first()
        if not task:
            return make_response({"error":"ToDo Not Found"}, 404)
        try:
            data = request.get_json()
            for key in data.keys():
                setattr(task, key, data[key])
        except:
            return make_response({"error":"Validation error, unprocessable entity"}, 422)
        try:
            db.session.add(task)
            db.session.commit()
        except:
            return make_response({"error":"Validation error, unprocessable entity"}, 422)
        return make_response(task.to_dict(), 200)

@app.route('/webhook', methods=["POST"])
def hook():
    print(request.data)
    return "Hello World"
    
#custom route for webscraper
@app.route('/fetchjobs')
def getjobs():
    oddball_jobs = scraper.scrapeOddball()
    return make_response(oddball_jobs)
    

api.add_resource(Home, '/')
api.add_resource(Quotes, '/quotes')
api.add_resource(ToDos, '/todos' )
api.add_resource(ToDoById, '/todos/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)