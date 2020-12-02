
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

recdata={
    "location": "val",
    "institution": "val",
    "degree_type": "val",
    "doc_id": "val",
    "university": "val",
    "score": "val",
    "year_of_completion": "val",
    "highest_degree": "val"
}



def hello_world(request):
    recdata = flask.request.json


    location = recdata['location']
    doc_id=recdata['doc_id']
    institution = recdata['institution']
    degree_type = recdata['degree_type']
    university = recdata['university']
    score = recdata['score']
    year_of_completion = recdata['year_of_completion']
    highest_degree = recdata['highest_degree']

    docs = db.collection("Profile").document(doc_id).collection("EducationDetails").where('highest_degree', '==', highest_degree).stream()

    for doc in docs:
        response = {
            "status": "False",
            "message": "EducationDetails exists already!"
        }
        return jsonify(response)

    ref = db.collection("Profile").document(doc_id).collection("EducationDetails").document()

    data = {
    "location": location,
    "institution": institution,
    "degree_type": degree_type,
    "doc_id": doc_id,
    "university": university,
    "score": score,
    "year_of_completion":year_of_completion,
    "highest_degree": highest_degree
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Educational Details added successfully!"
    }

    return jsonify(response)
