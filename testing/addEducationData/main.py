
import firebase_admin
from firebase_admin import credentials, firestore
import  flask
from flask import jsonify

cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-6bcb0d65ae.json')

firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': 'https://folk-database.firebaseio.com/'
                              })

db =firestore.client()

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

    ref = db.collection("Profile").document(doc_id).collection("Educational_Details").document()

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
