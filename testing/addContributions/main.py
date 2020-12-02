

# This function is to add the contribution

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify
import time

# initialize firebase application
firebase_admin.initialize_app()


# cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-6bcb0d65ae.json')
#
# firebase_admin.initialize_app(cred,
#                               {
#                                   'databaseURL': 'https://folk-database.firebaseio.com/'
#                               })

# connect to db
db = firestore.client()


# global variables
recdata = {

        "custom_fields":[{"q1": "Why should you be hired for this role?", "q1_response": 'sahdashj'},
                    {"q2": "Are you available for 2 months, starting immediately, for a work from home internship?", "q2_response": "sdkuasdl"}],
        "channel": "Frontend",
        "doc_id": "sjdksadkka",
        "contribution_level": "Intern",
        "action_taken": "Joined",
        "status": "Active",
        "contribution_type": "Full-time",
        "contribution_details": "get exp"
}

def hello_world(request):
    recdata = flask.request.json
    # print("Received Data :", recdata)

    # q1 = "Why should you be hired for this role?"
    # q2 = "Are you available for 2 months, starting immediately, for a work from home internship?"

    # q1 = recdata['custom_fields'].['q1']
    # q1_response = recdata['custom_fields']['q1_response']
    # q2 = recdata['custom_fields']['q2']
    # q2_response = recdata['custom_fields']['q2_response']


    custom_fields = recdata['custom_fields']

    channel = recdata['channel']
    contribution_level = recdata['contribution_level']
    action_taken = recdata['action_taken']
    status = recdata['status']
    contribution_type = recdata['contribution_type']
    contribution_details = recdata['contribution_details']


    docref = db.collection('test').document()
    cdoc = docref.collection('Contribution').document()


    data = {"custom_fields": firestore.ArrayUnion(custom_fields),
            "channel": channel,
            "timestamp": int(time.time()),
            "doc_id": docref.id,
            "contribution_level": contribution_level,
            "action_taken": action_taken,
            "status": status,
            "contribution_type": contribution_type,
            "contribution_details": contribution_details}

    cdoc.set(data)

    response = {
        "status": "True",
        "message": "Created Contributions"
    }
    # return jsonify(response)


# hello_world(recdata)