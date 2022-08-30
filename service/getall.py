from flask_restful import Resource
from flask import  request, jsonify, make_response
from models import Item, toDoList

class getAllToDos(Resource):
    def get(self):
        return make_response(jsonify(toDoList),200)

class createNewNote(Resource):
    def post(self):
        note_title = request.get_json()
        new_note = {}
        new_note['todo'] = []
        new_note['completed'] = []
        toDoList[note_title['title']] = new_note
        return make_response(jsonify({"message":"success"}), 201)

class createNewToDoItem(Resource):
    def post(self):
        note_info= request.get_json()
        if note_info['note_title'] not in toDoList.keys():
            return make_response(jsonify({"message":"Note doesn't exist"}), 404)
        note_title = note_info['note_title']
        del note_info['note_title']
        item=Item(**note_info)
        toDoList[note_title]['todo'].append(item.toJson())
        return make_response(jsonify({"message":"success"}), 201)

class completeItem(Resource):
    def post(self):
        note_info= request.get_json()
        if note_info['note_title'] not in toDoList.keys():
            return make_response(jsonify({"message":"Note doesn't exist"}), 404)
        note_title = note_info['note_title']
       
        for item in toDoList[note_title]['todo']:
            if item['id'] == note_info['id']:
                toDoList[note_title]['completed'].append(item)
                toDoList[note_title]['todo'].remove(item)   
                return make_response(jsonify({"message":"success"}), 201)
      
        return make_response(jsonify({"message":"item not found"}), 404)

class deleteToDoItemById(Resource):
    def delete(self):
        note_info= request.get_json()
        note_title = note_info['note_title']
        if note_title not in toDoList.keys():
            return make_response(jsonify({"message":"Note doesn't exist"}), 404)

        for li in toDoList[note_title]['todo']:
            if li['id'] == note_info['id']:
                toDoList[note_title]['todo'].remove(li)
                return make_response(jsonify({"message":"item removed successfully"}),200)
        for li in toDoList[note_title]['completed']:
            if li['id'] == note_info['id']:
                toDoList[note_title]['completed'].remove(li)
                return make_response(jsonify({"message":"item removed successfully"}),200)
        
        return make_response(jsonify({"message":"item does not exist"}),404)


class deleteNote(Resource):
    def delete(self):
      
        note_info= request.get_json()
        title = note_info['note_title']
        if title in toDoList.keys():
            del toDoList[title]

            return make_response(jsonify({"message":"deleted note successfully"}),200)
        else:
            return make_response(jsonify({"message":"note does not exist"}),404)


        