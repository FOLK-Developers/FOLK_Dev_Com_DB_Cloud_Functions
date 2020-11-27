import time
import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

# global variables
recData = {'doc_id': "ae4sChLW7MmmdbH56vOi",
           'url': "email@gmail.com",
           'domain': "google",
           'type': "communication",
           'user_name': "email",
           'signin_status': True,
           'performer': "Admin",
           'uid': 'xyz'}

verification_status = "Pending"
verified_by = "None"
verified_timestamp = 0


def hello_world(request):
    recData = flask.request.json
    # print("Received Data :", recdata)

    doc_id = recData['doc_id']
    url = recData['url']
    domain = recData['domain']
    type = recData['type']
    user_name = recData['user_name']
    signin_status = recData['signin_status']
    uid = recData['uid']

    if signin_status == True:
        verification_status = "Verified"
        verified_by = "domain"
        verified_timestamp = int(time.time())

    creation_timestamp = int(time.time())

    data = {
        'doc_id': doc_id,
        'url': url,
        'domain': domain,
        'type': type,
        'user_name': user_name,
        'update_timestamp': creation_timestamp,
        'verification_status': verification_status,
        'verified_by': verified_by,
        'verified_timestamp': verified_timestamp,
        'uid': uid
    }

    # your logic or code here..
    docref = db.collection('Profile').document(doc_id).collection('LinkedProfiles').document()
    docref.set(data)

    data = {
        'visibility_to_user': "Visible",
        'activity_type': "Data update",
        'category': "LinkedProfile",
        'sub_category': "createLinkedProfile",
        'details': domain,
        'sub_details': url,
        'performer': recData['performer'],
        'edate': int(time.time()),
        'doc_id': doc_id,
        'readable_date': firestore.SERVER_TIMESTAMP,
        'access_permission': ['admin']
    }

    docref = db.collection('Profile').document(doc_id).collection('Activities').document()
    docref.set(data)


    response = {
        "status": "True",
        "message": "Created Linked Profiles & Activities"
    }

    return jsonify(response)
