from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from service.getall import getAllToDos, createNewToDoItem, deleteToDoItemById, deleteNote, createNewNote, completeItem
from flask_apscheduler import APScheduler


app = Flask(__name__)
cors = CORS(app, resources={r"*":{"origins":"*"}})
api = Api(app)
api.add_resource(getAllToDos, "/getalltodos")
api.add_resource(createNewToDoItem, "/createnew")
api.add_resource(deleteToDoItemById, "/deleteitem")
api.add_resource(deleteNote, "/deletenote")
api.add_resource(createNewNote, "/createnote")
api.add_resource(completeItem, "/completeItem")

if __name__ == "__main__":
    app.debug=True
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run()
