# documentTestDup

# This code is for addDocuments. It checks for any duplicates.
# Eg : if resume already exists then it will change only the doc_link and keep previous info
# Otherwise it will create a new document

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-6bcb0d65ae.json')
#
# firebase_admin.initialize_app(cred,
#                               {
#                                   'databaseURL': 'https://folk-database.firebaseio.com/'
#                               })

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

    reference_file_name = recdata['reference_file_name']
    file_type = recdata['file_type']
    doc_link = recdata['doc_link']
    uploaded_by = recdata['uploaded_by']
    edate = recdata['edate']
    doc_type = recdata['doc_type']
    doc_id = recdata['doc_id']

    # Checking if the document alreday exists
    docs = db.collection('test').document(doc_id).collection('Documents').where('doc_link', '==', doc_link).where('reference_file_name', '==', reference_file_name)
    docref = docs.stream()

    # if it exists then we update only the doc_link and keep the rest same
    for doc in docref:
        data = {
            "reference_file_name": doc.to_dict()['reference_file_name'],
            "file_type": doc.to_dict()['file_type'],
            "doc_link": doc_link,
            "uploaded_by": doc.to_dict()['uploaded_by'],
            "edate": doc.to_dict()['edate'],
            "doc_type": doc.to_dict()['doc_type'],
            "doc_id": doc.to_dict()['doc_id']
        }

        alreadyExistingDoc = db.collection('test').document(doc_id).collection('Documents').document(doc.id)
        alreadyExistingDoc.set(
            data,
            merge=True
        )

        return jsonify(
            {
                "status": "True",
                "message": "Document exists already! Updated! "
            })

    # If it does'nt exist then we need to make a new documenet and add new data to it
    newDoc = db.collection('test').document(doc_id).collection('Documents').document()
    data = {
        "reference_file_name": reference_file_name,
        "file_type": file_type,
        "doc_link": doc_link,
        "uploaded_by": uploaded_by,
        "edate": edate,
        "doc_type": doc_type,
        "doc_id": doc_id
    }

    newDoc.set(data)

    response = {
        "status": "True",
        "message": "Document added successfully! "
    }

    return jsonify(response)
