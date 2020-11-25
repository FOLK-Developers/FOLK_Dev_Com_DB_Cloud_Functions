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
profileData = {}

def hello_world(request):
    recdata = flask.request.json
    print("Received Data :", recdata)

    #your logic or code here..
    prePrimaryData = db.collection_group(u'Pre Primary Info')
    docs = prePrimaryData.stream()
    for doc in docs:
        # print(f'{doc.id} => {doc.to_dict()}')
        print(doc.to_dict().keys())
        data = doc.to_dict().keys()
        for item in data:
            profileData[item] = "ha"
        break


    PrimaryData = db.collection_group(u'Primary Info')
    docs = PrimaryData.stream()
    for doc in docs:
        # print(f'{doc.id} => {doc.to_dict()}')
        print(doc.to_dict().keys())
        data = doc.to_dict().keys()
        for item in data:
            profileData[item] = "ha"
        break

    # repeat the above code for other sub collections

    # loading profile schema
    profileRef = db.collection('Profile').document()
    profileRef.set(profileData)

    response = {
        "status": "True",
        "message": " "
    }

    return jsonify(response)
