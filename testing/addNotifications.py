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
 "title": "val",
 "doc_id": "val",
 "notification_type": "val",
 "user_visibility": "val",
 "action_taken": "val",
 "message": "val",
 "application": "val",
 "image": "val",
 "edate": "val",
 "link": "val"
}


def hello_world(request):
    recdata = flask.request.json

    title = recdata['title']
    user_visibility = recdata['user_visibility']
    doc_id = recdata['doc_id']
    notification_type = recdata['notification_type']
    action_taken = recdata['action_taken']
    message = recdata['message']
    application = recdata['application']
    image = recdata['image']
    edate = int(time.time())
    link = recdata['link']

    docs = db.collection("Profile").document(doc_id).collection("Notifications").where('title', '==', title).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "Notifications exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("Notifications").document()

    data = {
        "title": title,
        "user_visibility": user_visibility,
        "notification_type": notification_type,
        "doc_id": doc_id,
        "action_taken": action_taken,
        "message": message,
        "application": application,
        "image": image,
        "edate": edate,
        "link": link
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Notifications added successfully!"
    }

    return jsonify(response)
