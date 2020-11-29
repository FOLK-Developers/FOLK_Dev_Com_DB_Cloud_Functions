import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

#global variables

def hello_world(request):
    recdata = flask.request.json

    evaluation = recdata['evaluation']
    doc_id = recdata['doc_id']
    evaluated_by = recdata['evaluated_by']
    name_of_skill = recdata['name_of_skill']

    docref = db.collection_group('Skills').where('name_of_skill', '==', name_of_skill)
    docs = docref.stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "Skill exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("Skills").document()

    data = {
        "evaluation": evaluation,
        "doc_id": doc_id,
        "evaluated_by": 'Admin',
        "name_of_skill": name_of_skill
    }

    ref.set(data)

    ref = db.collection("Profile").document(doc_id)

    data = {
        "skills": firestore.ArrayUnion([name_of_skill])
    }

    ref.update(data)

    response = {
        "status": "True",
        "message": "Skill added successfully!"
    }

    return jsonify(response)
