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
 "hours": "val",
 "rewards": "val",
 "major_contribution": "val",
 "join_date": "val",
 "status": "val",
 "exit_date": "val",
 "remarks": "val",
 "hr_manager": "val",
 "role": "val",
 "reporting_manager": "val",
 "doc_id": "val",
 "project_id": "val",
 "accesses": "val"
}


def hello_world(request):
    recdata = flask.request.json

    hours = recdata['hours']
    rewards = recdata['rewards']
    major_contribution = recdata['major_contribution']
    join_date = recdata['join_date']
    status = recdata['status']
    exit_date = recdata['exit_date']
    remarks = recdata['remarks']
    hr_manager = recdata['hr_manager']
    role = recdata['role']
    reporting_manager = recdata['reporting_manager']
    doc_id = recdata['doc_id']
    project_id = recdata['project_id']
    accesses = recdata['accesses']

    docs = db.collection("Profile").document(doc_id).collection("Projects").where('project_id', '==', project_id).where('join_date', '==', join_date).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "Project exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("Projects").document()

    data = {
        "hours": hours,
        "rewards": rewards,
        "major_contribution": major_contribution,
        "join_date": join_date,
        "status": status,
        "exit_date": exit_date,
        "hr_manager": hr_manager,
        "role": role,
        "reporting_manager": reporting_manager,
        "remarks": remarks,
        "doc_id": doc_id,
        "project_id": project_id,
        "accesses": accesses
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Projects added successfully!"
    }

    return jsonify(response)
