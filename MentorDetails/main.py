import firebase_admin
from firebase_admin import firestore
import requests
import flask
import time
import json
import datetime
from pytz import timezone
import pytz
from flask import request, jsonify

from firebase_admin import credentials

cred = credentials.Certificate('testing-bf5a4-firebase-adminsdk-k3wvf-9481825d20.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_name(name):
    coll = db.collection("Profile").where(u'name', '==', name).get()

    for docs in coll:
        doc = docs.to_dict()
    
    guide=doc['folk_guide']
    details=mentor_details(guide)
    return details

 def mentor_details(guide):
     coll1 = db.collection("Profile").where(u'name', '==', guide).get()
     for docs in coll1:
         doc=docs.to_dict()
     return doc

final_data=get_name("Sanjay Kumar Sah")
