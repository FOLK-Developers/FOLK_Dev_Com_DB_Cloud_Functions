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

    username=recdata['username']
    account_status =recdata['account_status']
    avatar=recdata['avatar']
    application=recdata['application']
    last_login=recdata['last_login']
    first_login=recdata['first_login']
    login_type=recdata['login_type']

    #Just a flag
    status = False


    doc_ref = db.collection(u'LoginInfo').where("username", "==", username).limit(1).stream()
    for doc in doc_ref:
        doc_id = doc.id  # userid is same as docid in ProfileInfo collection

    # getting the document associated with userid of current user
    doc = db.collection(u'ProfileInfo').where("userid", "==", doc_id)

    status=False

    try:
        doc.set(
            {
            "LoginInfo": {
            "username": username,
            "account_status": account_status,
            "avatar": avatar,
            "application": application,
            "last_login": last_login,
            "first_login": first_login,
            "login_type": login_type,
            "doc_id": doc_id
        }
            }
        )
        status=True

    except:
        status=False

    response = {
        "status": status,
        "message": "Login Info added successfully "
    }

    return jsonify(response)
