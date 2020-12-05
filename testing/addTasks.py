import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

recdata = {
 "completion_percent": "val",
 "date_of_completion": "val",
 "date_of_creation": "val",
 "date_of_due": "val",
 "description": "val",
 "doc_id": "val",
 "image": "val",
 "reward": "val",
 "status": "val",
 "title": "val"
}


def hello_world(request):
    recdata = flask.request.json

    completion_percent = recdata['completion_percent']
    date_of_completion = recdata['date_of_completion']
    date_of_creation = int(time.time())
    date_of_due = recdata['date_of_due']
    description = recdata['description']
    doc_id = recdata['doc_id']
    reward = recdata['reward']
    image = recdata['image']
    status = recdata['status']
    title = recdata['title']

    docs = db.collection("Profile").document(doc_id).collection("Tasks").where('title', '==', title).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "Tasks exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("Tasks").document()

    data = {
        "title": title,
        "completion_percent": completion_percent,
        "date_of_completion": date_of_completion,
        "doc_id": doc_id,
        "date_of_creation": date_of_creation,
        "date_of_due": date_of_due,
        "description": description,
        "image": image,
        "reward": reward,
        "status": status
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Tasks added successfully!"
    }

    return jsonify(response)
