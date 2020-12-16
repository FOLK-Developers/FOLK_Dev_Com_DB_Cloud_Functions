
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import flask
from flask import request, jsonify
from datetime import date
from datetime import datetime
from flask import request, jsonify

cred = credentials.Certificate('test-c0029-firebase-adminsdk-101ll-9923968a69.json')
firebase_admin.initialize_app(cred)
db = firestore.client()



# firebase_admin.initialize_app()
# db = firestore.client()




referral={'amount':'0','referral_name':'','referral_profile_id':'','referral_email_id':'','doc_id':'1'}
amount=referral['amount']
referral_name=referral['referral_name']
referral_profile_id=referral['referral_profile_id']
referral_email_id=referral['referral_email_id']
doc_id4=referral['doc_id']

data4={'amount':amount,'referral_name':referral_name,'referral_profile_id':referral_profile_id,'time':int(time.time()),'referral_email_id':referral_email_id,'doc_id':doc_id4}

ref4 = db.collection("ProfileTest").document(doc_id4).collection("ReferralSchemeFeature").document()
ref4.set(data4)

