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
 "meeting_venue": "val",
 "meeting_end_time": "val",
 "meeting_start_time": "val",
 "meeting_type": "val",
 "doc_id": "val",
 "attended_status": "val",
 "edate": "val",
 "confirmation_status": "val",
 "invite_status": "val",
 "meeting_location": "val",
 "meeting_category": "val",
 "meeting_id": "val",
 "hosted_by": "val"
}


def hello_world(request):
    recdata = flask.request.json

    meeting_venue = recdata['meeting_venue']
    meeting_start_time = recdata['meeting_start_time']
    meeting_end_time = recdata['meeting_end_time']
    meeting_type = recdata['meeting_type']
    doc_id = recdata['doc_id']
    attended_status = recdata['attended_status']
    edate = int(time.time())
    confirmation_status = recdata['confirmation_status']
    invite_status = recdata['invite_status']
    meeting_location = recdata['meeting_location']
    meeting_category = recdata['meeting_category']
    meeting_id = recdata['meeting_id']
    hosted_by = recdata['hosted_by']

    docs = db.collection("Profile").document(doc_id).collection("Meeting").where('meeting_id', '==', meeting_id).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "Meeting exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("Meeting").document()

    data = {
        "meeting_venue": meeting_venue,
        "meeting_start_time": meeting_start_time,
        "meeting_end_time": meeting_end_time,
        "meeting_type": meeting_type,
        "doc_id": doc_id,
        "attended_status": attended_status,
        "edate": edate,
        "confirmation_status": confirmation_status,
        "invite_status": invite_status,
        "meeting_location": meeting_location,
        "meeting_category": meeting_category,
        "meeting_id": meeting_id,
        "hosted_by": hosted_by
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Meeting added successfully!"
    }

    return jsonify(response)
