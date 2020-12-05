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
 "end_date": "val",
 "company_name": "val",
 "doc_id": "val",
 "company_location": "val",
 "start_date": "val",
 "status": "val",
 "designation": "val"
}




def hello_world(request):
    recdata = flask.request.json

    end_date = recdata['end_date']
    company_name = recdata['company_name']
    doc_id = recdata['doc_id']
    company_location = recdata['company_location']
    start_date = recdata['start_date']
    status = recdata['status']
    designation = recdata['designation']

    docs = db.collection("Profile").document(doc_id).collection("ProfessionalDetails").where('company_name', '==', company_name).where('start_date', '==', start_date).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "ProfessionalDetails exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("ProfessionalDetails").document()

    data = {
        "end_date": end_date,
        "company_name": company_name,
        "company_location": company_location,
        "doc_id": doc_id,
        "start_date": start_date,
        "status": status,
        "designation": designation
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "ProfessionalDetails added successfully!"
    }

    return jsonify(response)
