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
 "purpose": "val",
 "creation_timestamp": "val",
 "doc_id": "val",
 "doer_docid": "val",
 "dnd": "val",
 "status": "val"
}

recdata1 = {
 "type_of_followup": "val",
 "details": "val",
 "doc_id": "val",
 "doer_docid": "val",
 "follow_up_id": "val",
 "edate": "val"
}

def hello_world(request):
    recdata = flask.request.json

    purpose = recdata['purpose']
    creation_timestamp = int(time.time())
    doc_id = recdata['doc_id']
    doer_docid = recdata['doer_docid']
    dnd = True
    status = recdata['status']

    type_of_followup = recdata1['type_of_followup']
    details = recdata1['details']
    # doc_id = recdata1['doc_id']
    # doer_docid = recdata1['doer_docid']
    # follow_up_id = recdata1['follow_up_id']
    edate = int(time.time())

    docs = db.collection("Profile").document(doc_id).collection("FollowUps").where('doer_docid', '==', doer_docid).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "FollowUps exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("FollowUps").document()

    follow_up_id = ref.id
    ref1 = db.collection("test").document("sample").collection("FollowUps").document(follow_up_id).collection("FollowUpDetails").document()

    data = {
        "purpose": purpose,
        "creation_timestamp": creation_timestamp,
        "doer_docid": doer_docid,
        "doc_id": doc_id,
        "dnd": dnd,
        "status": status
    }

    ref.set(data)

    data1 = {
        "type_of_followup": type_of_followup,
        "details": details,
        "doer_docid": doer_docid,
        "doc_id": doc_id,
        "follow_up_id": follow_up_id,
        "edate": edate
    }

    ref1.set(data1)

    response = {
        "status": "True",
        "message": "FollowUps and FollowUpDetails added successfully!"
    }

    return jsonify(response)
