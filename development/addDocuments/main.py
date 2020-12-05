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

# global variables

recdata = {
    "reference_file_name": "reference_file_name2",
    "file_type": "file_type1",
    "doc_link": "doc_link4",
    "uploaded_by": "uploaded_by1",
    "edate": "edate1",
    "doc_type": "doc_type1",
    "doc_id": "ED55tzInA5Xm4jctf7TO"
}


def hello_world(request):
    recdata = flask.request.json

    # your logic or code here..

    doc_id = recdata['doc_id']
    reference_file_name = recdata['reference_file_name']
    file_type = recdata['file_type']
    doc_link = recdata['doc_link']
    uploaded_by = recdata['uploaded_by']
    edate = int(time.time())
    doc_type = recdata['doc_type']

    docs = db.collection('Profile').document(doc_id).collection('Documents').where('doc_link', '==', doc_link).where('reference_file_name', '==', reference_file_name).stream()

    for doc in docs:
        data = {
            "reference_file_name": doc.to_dict()['reference_file_name'],
            "file_type": doc.to_dict()['file_type'],
            "doc_link": doc_link,
            "uploaded_by": doc.to_dict()['uploaded_by'],
            "edate": doc.to_dict()['edate'],
            "doc_type": doc.to_dict()['doc_type'],
            "doc_id": doc.to_dict()['doc_id']
        }

        alreadyExistingDoc = db.collection('Profile').document(doc_id).collection('Documents').document(doc.id)
        alreadyExistingDoc.set(
            data,
            merge=True
        )

        return jsonify(
            {
                "status": "True",
                "message": "Document exists already! Updated! "
            })

    ref = db.collection('Profile').document(doc_id).collection('Documents').document()

    data = {
        "reference_file_name": reference_file_name,
        "file_type": file_type,
        "doc_link": doc_link,
        "uploaded_by": uploaded_by,
        "edate": edate,
        "doc_type": doc_type,
        "doc_id": doc_id
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Documents added successfully!"
    }

    return jsonify(response)
