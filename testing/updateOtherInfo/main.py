# updateOtherInfo : Other info like linked profiles, skills and projects are updated/modified in db

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
    
    #Getting username and data from front-end 
    # The fields will be prepopulated with old info, so user can just change those with new info, so we can get all fields from front end
    username = recdata['username'] # or we can use session management and get the userinfo
    url = recdata['url']
    domain = recdata['domain']
    profile_type = recdata['type']
    user_name = recdata['user_name']
    skill = recdata['skill']
    evaluation = recdata['evaluation']
    evaluated_by = recdata['evaluated_by']
    project_id = recdata['project_id']
    role = recdata['role']
    status = recdata['status']
    major_contribution = recdata['major_contribution']
    hours = recdata['hours']
    start_date = recdata['start_date']
    end_date = recdata['end_date']
    reporting_manager = recdata['reporting_manager']
    hr_manager = recdata['hr_manager']
    accesses = recdata['accesses']
    rewards = recdata['rewards']

    # getting the docid using username
    doc_ref = db.collection(u'LoginInfo').where("username","==",username).limit(1).stream()
    for doc in doc_ref:
        userid = doc.id #userid is same as docid in ProfileInfo collection

    # getting the document associated with userid of current user
    doc = db.collection(u'ProfileInfo').where("userid","==",userid)

    # Update existing doc with new data of "linkedProfiles", "skills" and "projects" sub-coll in collection 'ProfileInfo'
    try:
        doc.update({
            u'LinkedProfiles':{
                u'url,':url,
                u'domain': domain,
                u'type': profile_type,
                u'user_name':user_name,
                u'update_timestamp': datetime.now() #it will take time at which the doc is updated
                },

            u'Skills':{
                u'name_of_skill':skill,
                u'evaluation':evaluation,
                u'evaluated_by':evaluated_by
            },
            u'Projects':{
                u'project_id': project_id,
                u'role':role,
                u'status':status,
                u'start_date':start_date,
                u'end_date':end_date,
                u'major_contribution':major_contribution,
                u'hours':hours,
                u'reporting_manager': reporting_manager,
                u'hr_manager': hr_manager,
                u'accesses': accesses,
                u'rewards': rewards
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
