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
    email = recdata['email']
    userAccessLevel = recdata['user-access-level']
    dataLevel = recdata['data-level']
    primarySource = recdata['primary-source']
    secondarySource = recdata['secondary-source']
    name = recdata['name']

    pre_primary = {
        "name": name,
        "email": email,
        "user_access_level": userAccessLevel,
        "data_level": dataLevel,
        "primary_source": primarySource,
        "secondary_source": secondarySource
    }

    docref = db.collection("PrePrimaryInfo").document()
    docref.set(pre_primary)

    # For Example
    # secondary = {
    #     "name": name,
    #     "email": email,
    #     "user_access_level": userAccessLevel,
    #     "data_level": dataLevel,
    #     "primary_source": primarySource,
    #     "secondary_source": secondarySource
    # }
    #
    #
    # docref = db.collection("Secondary").document()
    # docref.set(secondary)


    response = {
        "status" : "True",
        "message" : "You Are Registered"
    }
    return jsonify(response)
