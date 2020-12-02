import time

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

    doc_id = recdata["doc_id"]
    last_login = int(time.time())
    first_login = int(time.time())
    application = recdata['application']
    avatar = recdata["avatar"]
    login_type = recdata["login_type"]
    account_status = recdata["account_status"]
    username = recdata["username"]

    flogin = 0

    docs = db.collection("Profile").document(doc_id).collection("LoginInfo").where('login_type', '==', login_type).stream()

    ref = db.collection("Profile").document(doc_id).collection("LoginInfo").document()

    for doc in docs:
        flogin = 1

    if flogin:
        ref.set({
            "doc_id": doc_id,
            "last_login": last_login,
            "application": application,
            "avatar": avatar,
            "login_type": login_type,
            "account_status": account_status,
            "username": username}, merge=True)
    else:
        ref.set({
            "doc_id": doc_id,
            "last_login": last_login,
            "first_login": first_login,
            "application": application,
            "avatar": avatar,
            "login_type": login_type,
            "account_status": account_status,
            "username": username})

    return jsonify()
