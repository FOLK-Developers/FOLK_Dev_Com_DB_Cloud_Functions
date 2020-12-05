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
 "rewarder_id": "val",
 "purpose": "val",
 "doc_id": "val",
 "voucher_type": "val",
 "voucher_value": "val",
 "edate": "val"
}



def hello_world(request):
    recdata = flask.request.json

    rewarder_id = recdata['rewarder_id']
    purpose = recdata['purpose']
    doc_id = recdata['doc_id']
    voucher_type = recdata['voucher_type']
    voucher_value = recdata['voucher_value']
    edate = int(time.time())

    docs = db.collection("Profile").document(doc_id).collection("Rewards").where('rewarder_id', '==', rewarder_id).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "Rewards exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("Rewards").document()

    data = {
        "rewarder_id": rewarder_id,
        "purpose": purpose,
        "voucher_type": voucher_type,
        "doc_id": doc_id,
        "voucher_value": voucher_value,
        "edate": edate
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Rewards added successfully!"
    }

    return jsonify(response)
