
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




products={'cost':'0','discounts':'0','image_link':'0','name':'','type':'','size':'0','doc_id':'1'}
cost=products['cost']
discount=products['discounts']
image_link=products['image_link']
name=products['name']
type=products['type']
size=products['size']
doc_id3=products['doc_id']

data3={'cost':cost,'discount':discount,'image_link':image_link,'name':name,'product_type':type,"size":size,'doc_id':doc_id3}

ref3 = db.collection("ProfileTest").document(doc_id3).collection("ProductsFeature").document()
ref3.set(data3)


