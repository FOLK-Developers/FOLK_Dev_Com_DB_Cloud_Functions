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
    
    # The fields will be prepopulated with old info, so user can just change those with new info, so we can get all fiels from front end
    username = recdata['username']
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

    # getting the docid using username
    doc_ref = db.collection(u'LoginInfo').where("username","==",username).limit(1).stream()
    for docu in doc_ref:
        userid = docu.id #userid is same as docid in ProfileInfo collection

    # getting the document associated with userid of current user
    doc = db.collection(u'ProfileInfo').where("userid","==",userid)

    # Update existing doc in collection 'ProfileInfo'
    try:
        doc.update({
            u'email': email,
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
        })
        status = "True"
    except:
        status = "False"

    #response object
    response = {
                "status": status
                }
    return jsonify(response)
