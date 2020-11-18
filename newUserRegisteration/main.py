import firebase_admin
import flask
# import pyfcm
from firebase_admin import credentials, messaging
from firebase_admin import firestore
# from datetime import date
# from datetime import datetime
from flask import request, jsonify
from pyfcm import FCMNotification

import urllib.request
import json
# import time
import requests
# import ast

firebase_admin.initialize_app()
db = firestore.client()


def hello_world(request):

    # PrePrimaryInfo
    recdata = flask.request.json
    name = recdata['name']
    email = recdata['email']
    userAccessLevel = recdata['user-access-level']
    dataLevel = recdata['data-level']
    primarySource = recdata['primary-source']
    secondarySource = recdata['secondary-source']

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

    # PrimaryInfo
    recdata = flask.request.json
    phoneNo = recdata['phone-no']
    currentWorkingLocation = recdata['current-working-location']
    city = recdata['city']
    state = recdata['state']
    country = recdata['country']
    pincode = recdata['pincode']
    dob = recdata['dob']
    gender = recdata['gender']

    primary = {
        "phone_no": phoneNo,
        "current_working_location": currentWorkingLocation,
        "city": city,
        "state": state,
        "country": country,
        "pincode": pincode,
        "dob": dob,
        "gender": gender
    }

    docref = db.collection("PrimaryInfo").document()
    docref.set(primary)

    # SecondaryInfo
    recdata = flask.request.json
    interests = recdata['interests']
    contributions = recdata['contributions']
    skills = recdata['skills']

    secondary = {
        "interests": interests,
        "contributions": contributions,
        "skills": skills,
    }

    docref = db.collection("SecondaryInfo").document()
    docref.set(secondary)

    # TertiaryInfo
    recdata = flask.request.json
    socialMediaProfiles = recdata['social-media-profiles']
    collegeDetails = recdata['college-details']
    comapanyDetails = recdata['comapany-details']
    userAccessLevel = recdata['user-access-level']
    photo = recdata['photo']

    tertiary = {
        "social_media_profiles": socialMediaProfiles,
        "college-details": collegeDetails,
        "comapany-details": comapanyDetails,
        "user-access-level": userAccessLevel,
        "photo": photo
    }

    docref = db.collection("TertiaryInfo").document()
    docref.set(tertiary)

    response = {
        "status" : "True",
        "message" : "You Are Registered"
    }
    return jsonify(response)
