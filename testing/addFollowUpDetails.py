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
 "type_of_followup": "val",
 "details": "val",
 "doc_id": "val",
 "doer_docid": "val",
 "follow_up_id": "val",
 "edate": "val"
}


def hello_world(request):
    recdata = flask.request.json

    type_of_followup = recdata['type_of_followup']
    details = recdata['details']
    doc_id = recdata['doc_id']
    doer_docid = recdata['doer_docid']
    follow_up_id = recdata['follow_up_id']
    edate = int(time.time())

    docs = db.collection("Profile").document(doc_id).collection("FollowUps").document(follow_up_id)

    flag = 0

    for doc in docs:
        flag = 1

    if flag == 0:
        response = {
            "status": "False",
            "message": "FollowUp does not exists!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("FollowUps").document(follow_up_id).collection("FollowUpDetails").document()

    data = {
        "type_of_followup": type_of_followup,
        "details": details,
        "doer_docid": doer_docid,
        "doc_id": doc_id,
        "follow_up_id": follow_up_id,
        "edate": edate
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "FollowUpDetails added successfully!"
    }

    return jsonify(response)
