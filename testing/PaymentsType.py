
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



payment={'paid_chaintanya_coins':'0','paid_rupees':'0','paid_amount':'0','payment_method':'0','doc_id':'1','type':'0'}
paid_chaintanya_coins=payment['paid_chaintanya_coins']
paid_rupees=payment['paid_rupees']
paid_amount=payment['paid_amount']
payment_method=payment['payment_method']
doc_id2=payment['doc_id']
type=payment['type']


data2={'paid_chaintanya_coins':paid_chaintanya_coins,'paid_rupees':paid_rupees,'time':int(time.time()),'paid_amount':paid_amount,'doc_id':doc_id2,'payment_type':type}

ref2 = db.collection("ProfileTest").document(doc_id2).collection("PaymentsFeature").document()
ref2.set(data2)


