import time
import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify

# initialize firebase application
firebase_admin.initialize_app()

# connect to db
db = firestore.client()

# global variables
recData = {
   "primary_source": "Social Media",
    "secondary_source": "Facebook",
   "url": "test@gmail.com",
   "domain": "google",
   "name": "Unknown",
   "signin_status": True,
   "performer": "Admin",
   "uid": "xyz"
}


# to get profile flags
def getProfileFlags(doc_id):
    docref = db.collection('Profile').document(doc_id)
    data = docref.get().to_dict()
    preprimary_infostatus = False
    primary_infostatus = False
    secondary_infostatus = False
    tertiary_infostatus = False
    name = 'Unknown Friend'
    response = {}
    if 'flags' in data.keys():
        if 'preprimary_infostatus' in data.keys()['flags']:
            preprimary_infostatus = data['flags']['preprimary_infostatus']
            print(preprimary_infostatus)
            response['preprimary_infostatus'] = preprimary_infostatus
        if 'primary_infostatus' in data.keys()['flags']:
            primary_infostatus = data['flags']['primary_infostatus']
            response['primary_infostatus'] = primary_infostatus
        if 'secondary_infostatus' in data.keys()['flags']:
            secondary_infostatus = data['flags']['secondary_infostatus']
            response['secondary_infostatus'] = secondary_infostatus
        if 'tertiary_infostatus' in data.keys()['flags']:
            tertiary_infostatus = data['flags']['tertiary_infostatus']
            response['tertiary_infostatus'] = tertiary_infostatus
    if 'name' in data.keys():
        name = data['name']

    return {"name": name, "preprimary_infostatus": preprimary_infostatus, 'secondary_infostatus': secondary_infostatus,
            'primary_infostatus': primary_infostatus, 'tertiary_infostatus': tertiary_infostatus}


def hello_world(request):
    recData = flask.request.json
    # print("Received Data :", recdata)

    domain = recData['domain']
    url = recData['url']
    secondary_source = recData['secondary_source']
    primary_source = recData['primary_source']
    name = recData['name']
    signin_status = recData['signin_status']
    performer = recData['performer']
    uid = recData['uid']

    # your logic or code here..

    docref = db.collection_group(u'LinkedProfiles').where(u'domain', u'==', domain).where('url', '==', url)
    docs = docref.stream()

    ldoc_id = ""
    vstatus = ""
    type = ""
    lpvstatus = False

    for doc in docs:
        # print(f'{doc.id} => {doc.to_dict()}')
        ldoc_id = doc.to_dict()['doc_id']
        vstatus = doc.to_dict()['verification_status']

    if ldoc_id != "":
        if vstatus == "Verified":
            lpvstatus = True
    else:
        docref = db.collection('Profile').document()
        docref.set({
            'secondary_source': secondary_source,
            'primary_source': primary_source,
            'name': name,
            'timestamps.preprimary_infostatus': int(time.time()),
            'flags.preprimary_infostatus': True,
            'user_access_level': ['public']
        })
        ldoc_id = docref.id
        if domain == 'mobile' or domain == 'email':
            type = "communication"
        elif domain == 'facebook' or domain == 'github' or domain == 'linkedin':
            type = "social"

        data = {'doc_id': ldoc_id,
                'url': url,
                'domain': domain,
                'type': type,
                'user_name': name,
                'signin_status': signin_status,
                'performer': performer,
                'uid': uid}

        lpvstatus = signin_status
        resp = requests.post('https://us-central1-folk-dev-com-db.cloudfunctions.net/createLinkedProfile',
                             json=data)

    flagsData = getProfileFlags(ldoc_id)

    response = {
        "verification_status": lpvstatus,
        "name": name,
        "flags.preprimary_infostatus": flagsData['preprimary_infostatus'],
        "doc_id": ldoc_id
        # 'secondary_infostatus': flagsData['secondary_infostatus'],
        # 'primary_infostatus': flagsData['primary_infostatus'],
        # 'tertiary_infostatus': flagsData['tertiary_infostatus'],
    }

    data = {
        'visibility_to_user': "Hidden",
        'activity_type': "Login",
        'category': "LinkedProfile",
        'sub_category': "linkedProfileExists",
        'details': domain,
        'sub_details': url,
        'performer': performer,
        'edate': int(time.time()),
        'doc_id': ldoc_id,
        'readable_date': firestore.SERVER_TIMESTAMP,
        'access_permission': ['admin']
    }

    docref = db.collection('Profile').document(ldoc_id).collection('Activities').document()
    docref.set(data)

    return jsonify(response)
