# registerNewUser

import firebase_admin
import flask
import pyfcm
from firebase_admin import credentials, messaging
from firebase_admin import firestore
from datetime import date
from datetime import datetime
from flask import request, jsonify
from pyfcm import FCMNotification

import urllib.request
import json
import time
import requests
import ast

firebase_admin.initialize_app()
db = firestore.client()

def hello_world(request):
    recdata = flask.request.json
    
    username = recdata['username']
    password = recdata['password']
    
    #checking if a/c exists with same username
    doc_ref = db.collection(u'LoginInfo').where("username","==",username).limit(1).stream()

    userData = []
    status = "True"
    for doc in doc_ref:
        status = "False"
        break

    #if do not exists then create one, else status = false
    if status:
        data = {
            u'username': username,
            u'password': password
        }
        # Add a new doc in collection 'LoginInfo'
        db.collection(u'LoginInfo').add(data)

        #response object
        response = {
                    "status": status,
                    "message": "New user registered successfully"
                    }
    
    else:
        #response object
        response = {
                    "status": status,
                    "message":"Username already exists"
                    }
    return jsonify(response)
