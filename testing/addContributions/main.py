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

#global variables

recdata={
    # "custom_fields": {'response':'val', 'title':'val'},
    "channel": "val",
    "timestamp": "val",
    "doc_id": "val",
    "contribution_level": "val",
    "action_taken": "val",
    "status": "val",
    "contribution_type": "val",
    "contribution_details": "val"
}

def hello_world(request):
    # recdata = flask.request.json
    print("Received Data :", recdata)

    #your logic or code here..

    # uid = recdata['uid']  # make sure

    # response = recdata['response']
    # title = recdata['title']
    # custom_fields =

    uid = 'None'

    channel= recdata['channel']
    contribution_level=recdata['contribution_level']
    action_taken = recdata['action_taken']
    status = recdata['status']
    contribution_type = recdata['contribution_type']
    contribution_details = recdata['contribution_details']

    doc_id = recdata['doc_id']

    # docs = db.collection('Profile').where('uid', '==', uid).limit(1).stream()

    ref = db.collection("Profile").document(doc_id).collection("Contributions").document()

    # id = ref.id # make sure

    timestamp = int(time.time())

    data={
        # "custom_fields": custom_fields,
        "channel": channel,
        "timestamp": timestamp,
        "doc_id": doc_id,
        "contribution_level":contribution_level,
        "action_taken": action_taken,
        "status": status,
        "contribution_type":contribution_type,
        "contribution_details": contribution_details,
        'uid': "None"
}

    ref.set(data)

    response = {
        "status": "True",
        "message": "Created Contributions"
    }

    return jsonify(response)
