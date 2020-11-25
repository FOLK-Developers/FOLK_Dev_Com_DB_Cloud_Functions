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
    # print("Received Data :", recdata)

    #your logic or code here..


    response = {
        "status": "True",
        "message": " "
    }

    return jsonify(response)
