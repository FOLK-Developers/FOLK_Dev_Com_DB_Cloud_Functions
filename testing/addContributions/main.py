import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify
from datetime import time

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

# global variables


def hello_world(request):
    recdata = flask.request.json
    # print("Received Data :", recdata)

    q1 = recdata['q1']
    q1_response = recdata['q1_response']

    # q1 = "Why should you be hired for this role?"
    # q2 = "Are you available for 2 months, starting immediately, for a work from home internship?"

    docref = db.collection('test').document()
    cdoc = docref.collection('Contribution').document()

    data = {"custom_fields": firestore.ArrayUnion([{"title": q1, "response": q1_response}]),
            "channel": "Backend",
            "timestamp": int(time.time()),
            "doc_id": docref.id,
            "contribution_level": "Intern",
            "action_taken": "Joined",
            "status": "Active",
            "contribution_type": "Full-time",
            "contribution_details": "get exp"}

    cdoc.set(data)

    response = {
        "status": "True",
        "message": "Created Contributions"
    }

    return jsonify(response)
