import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify
cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-999a6d8c63.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://folk-dev-com-db.firebaseio.com'
})
# # token = []
db = firestore.client()

upddata = {
    "name": "val",
    "mobile": "val",
    "city": "val",
    "primary_source": "val"
}

fields_array = ["name", "mobile", "city"]

for field_name in upddata.keys():
    if field_name in fields_array:
        ref = db.collection('test').document('sample')
        ref.update({field_name: upddata[field_name]})
    else:
        print(field_name, 'is not updatable')

data = {
    'visibility_to_user': "Hidden",
    'activity_type': "Update Profile",
    'category': "LinkedProfile",
    'sub_category': "linkedProfileExists",
    'edate': int(time.time()),
    'doc_id': 'w5pjetNFV7sG524EIqKS',
    'readable_date': firestore.SERVER_TIMESTAMP,
    'access_permission': ['admin']
}

docref = db.collection('test').document('sample').collection('Activities').document()
docref.set(data)
