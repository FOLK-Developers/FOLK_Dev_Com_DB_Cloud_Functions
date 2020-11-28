import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

#global variables

def hello_world(request):
    recdata = flask.request.json
    print("Received Data :", recdata)

    #your logic or code here..

    uid = recdata['uid'] # make sure
    reference_file_name = recdata['reference_file_name']
    file_type = recdata['file_type']
    doc_link = recdata['doc_link']
    uploaded_by = recdata['uploaded_by']
    edate = recdata['edate']
    doc_type = recdata['doc_type']




    docsInProfile = db.collection('Profile').where('uid', '==', uid).limit(1).stream()

    doc_id = ''
    for doc in docsInProfile:
        doc_id = doc.id

    docInDocument = db.collection('Profile').document(doc_id).collection('Documents').document()
    id = docInDocument.id # make sure

    data={
        "reference_file_name": "val",
        "file_type": "val",
        "doc_link": "val",
        "uploaded_by": "val",
        "edate": "val",
        "doc_type": "val",
        "doc_id": "val"
    }

    docInDocument.set(
        data
    )

    response = {
        "status": "True",
        "message": " "
    }

    return jsonify(response)
