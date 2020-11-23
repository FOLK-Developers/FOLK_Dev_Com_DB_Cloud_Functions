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
flag=0
pid=None
def hello_world(request):
    recdata = flask.request.json
    print("Received Data :", recdata)

    #your logic or code here..
    uname=recdata["uname"]
    pwd=recdata["password"]
    profile = db.collection(u'LoginInfo').where("username","==",uname).limit(1).stream()
    for doc in profile:
        flag=1
        pid=doc.to_dict()['profile_id']
    if flag:
        docref=db.collection('Profile').document(pid)
        name=docref.get().to_dict()['name']
        message=name+", Welcome to Folk Developers"
        response = {
            "status": "True",
            "message": message
        }
    else:
        response = {
            "status": "False",
            "message": " sorry, please check your credentials "
        }

    return jsonify(response)
