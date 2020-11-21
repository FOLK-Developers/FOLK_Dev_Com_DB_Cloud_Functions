import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request

# Use a service account
cred = credentials.Certificate('/home/sahil/Desktop/testapp-10f69-firebase-adminsdk-84avv-136ea6e1b7.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#Taking the sample data which will be later taken in request.json
record={
        "recdata" : {
            "description": "The task is to find out the cities belonging to UP and Delhi.",
            "startDate": "10-11-2020",
            "endDate": "15-11-2020"
        },
        "newDescription":"Take all the North Indian states",
        "newStartDate":"10-11-2020",
        "newStartDAte":"15-11-2020"
    }

def projectUpdater():
    # recdata = flask.request.json

#Updating the information
#Here the descriptions are swaped i.e new swaped with old description
    temp=record['recdata']['description']
    record['recdata']['description']=record['newDescription']
    record["newDescription"]=temp

    docRef=db.collection("record").document()
    docRef.set(record)

    return record

projectUpdater()


