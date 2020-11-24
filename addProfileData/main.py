# addProfileData : after account is created, user can later add extra data for profile

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
    
    uname = recdata['username']
    email = recdata['email']
    gender = recdata['gender']
    phone_no = recdata['phone_no']
    birth_date = recdata['birth_date']
    birth_month = recdata['birth_month']
    birth_year = recdata['birth_year']
    city = recdata['city']
    state = recdata['state']
    country = recdata['country']
    pincode = recdata['pincode']
    current = recdata['location_current']

    doc_ref = db.collection(u'LoginInfo').where("username","==",uname).limit(1).stream()
    for doc in doc_ref:
        userid = doc.id
    data = {
        u'email': email,
        u'userid': userid,
        u'gender': gender,
        u'mobile':phone_no,
        u'birth_date':birth_date,
        u'birth_year':birth_year,
        u'birth_month':birth_month,
        u'location_city':city,
        u'location_state':state,
        u'location_country':country,
        u'location_pincode':pincode,
        u'location_current':current,
        u'flags':{
            u'preprimary_info_status': True
        }
    }

    # Add a new doc in collection 'ProfileInfo'
    try:
        db.collection(u'Profile').add(data)
        status = "True"
    except:
        status = "False"

    #response obj
    response = {
                "status": status
                }
    return jsonify(response)
