import firebase_admin
from firebase_admin import credentials, firestore
import flask
from flask import jsonify

cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-999a6d8c63.json')

firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': "https://folk-dev-com-db.firebaseio.com"
                              })

db = firestore.client()

# getProfile doc ids
lpdocref = db.collection_group('LinkedProfiles').limit(2).stream()
lpcount = 0
for doc in lpdocref:
    print(doc.id)
    lpmdocref = db.collection('LinkedProfiles').document()
    data = doc.to_dict()
    lpmdocref.set(data)
    db.collection('Profile').document(data['doc_id']).collection('LinkedProfiles').document(doc.id).delete()