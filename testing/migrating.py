import firebase_admin
from firebase_admin import credentials, firestore
import flask
from flask import jsonify

cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-999a6d8c63.json')

firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': 'https://folk-database.firebaseio.com/'
                              })

db = firestore.client()

# getProfile doc ids
pdocref = db.collection('Profile').limit(1).stream()

pcount = 0
lpcount = 0

for doc in pdocref:
    # docid = doc.id
    lpdocref = db.collection('Profile').document(doc.id).collection('LinkedProfiles').stream()
    pcount += 1
    for lpdoc in lpdocref:
        lpmdocref = db.collection('LinkedProfiles').document()
        lpmdocref.set(lpdoc.to_dict())
        lpcount += 1

print("Total Profiles Updated: " + pcount)
print("Total Linked Profiles Updated: " + lpcount)