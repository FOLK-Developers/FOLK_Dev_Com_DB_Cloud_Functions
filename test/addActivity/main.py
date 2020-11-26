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

    visibility_to_user =recdata['visibility_to_user']
    category=recdata['category']
    details=recdata['details']
    edate=recdata['edate']
    performer=recdata['performer']
    sub_details=recdata['sub_details']
    sub_category=recdata['sub_category']
    readable_date=recdata['readable_date']
    Activity_type=recdata['sub_details']
    Access_permission=recdata['Access_permission']


    doc_ref = db.collection(u'LoginInfo').where("username","==",username).limit(1).stream()
    for doc in doc_ref:
        doc_id = doc.id #userid is same as docid in ProfileInfo collection

    # getting the document associated with userid of current user
    doc = db.collection(u'ProfileInfo').where("userid","==",doc_id)


    data={
       "visibility_to_user" :visibility_to_user,
        "category":category,
        "details":details,
        "edate":edate,
        "performer":performer,
        "sub_details":sub_details,
        "doc_id":doc_id,
        "sub_category":sub_category,
        "readable_date":readable_date,
        "Activity_type":Activity_type,
        "Access_permission":Access_permission

    }
    status=False

   #Adding data to db
    try:
        doc.set(data)
	status=True
    except:
        status=False
    response = {
        "status": status,
        "message": "Activity added successfully "
    }

    return jsonify(response)
