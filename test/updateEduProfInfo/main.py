# updateProfileInfo2 : profile info like education details and professional details can be updated/modified

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
    
    # The fields will be prepopulated with old info, so user can just change those with new info, so we can get all fields from front end
    username = recdata['username'] # or we can use session management and get the userinfo
    degree_type = recdata['degree_type']
    highest_degree = recdata['highest_degree']
    year_of_completion = recdata['year_of_completion']
    institute = recdata['institute']
    university = recdata['university']
    location = recdata['location']
    marks_scored = recdata['marks_scored']
    designation = recdata['designation']
    status = recdata['status']
    company = recdata['company']
    company_location = recdata['company_location']
    start_date = recdata['start_date']
    end_date = recdata['end_date']

    # getting the docid using username
    doc_ref = db.collection(u'LoginInfo').where("username","==",username).limit(1).stream()
    for doc in doc_ref:
        userid = doc.id #userid is same as docid in ProfileInfo collection

    # getting the document associated with userid of current user
    doc = db.collection(u'ProfileInfo').where("userid","==",userid)

    # Update "educationDetails" and "professionalDetails" sub-coll in collection 'ProfileInfo'
    try:
        doc.update({
            u'EducationDetails':{
                u'degree_type,':degree_type,
                u'highest_degree': highest_degree,
                u'year_of_completion': year_of_completion,
                u'institute':institute,
                u'university':university,
                u'marks_scored':marks_scored
            },
            u'ProfessionalDetails':{
                u'designation':designation,
                u'status':status,
                u'company':company,
                u'company_location':company_location,
                u'start_date':start_date,
                u'end_date':end_date
            }
        })
        status = "True"
    except:
        status = "False"

    #response object
    response = {
                "status": status
                }
    return jsonify(response)
