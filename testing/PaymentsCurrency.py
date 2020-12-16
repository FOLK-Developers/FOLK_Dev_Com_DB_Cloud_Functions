
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


#CURRENCY

coins={
 'gold_coins_spent':'0',
    'silver_coins_spent':'0',
    'copper_coins_spent':'0',
    'gold_coins_balance':'0',
    'silver_coins_balance': '0',
    'copper_coins_balance': '0',

    'doc_id':'1'

}
gold_coins_spent=coins['gold_coins_spent']
silver_coins_spent=coins['silver_coins_spent']
copper_coins_spent=coins['copper_coins_spent']
gold_coins_balance=coins['gold_coins_balance']
silver_coins_balance=coins['silver_coins_balance']
copper_coins_balance=coins['copper_coins_balance']
doc_id=coins['doc_id']


data={'doc_id':doc_id,'gold_coins_spent':gold_coins_spent,'silver_coins_spent':silver_coins_spent,'copper_coins_spent':copper_coins_spent,'gold_coins_balance':gold_coins_balance,'silver_coins_balance':silver_coins_balance,'copper_coins_balance':copper_coins_balance}

ref = db.collection("ProfileTest").document(doc_id).collection("ChaintanyaCurrency").document('fix').collection("ChaintanyaCoins").document()
ref.set(data)

money={'rupees_spent':'0',
       'rupees_balance':'0',
       'doc_id':'1'}

rupees_spent=money['rupees_spent']
rupees_balance=money['rupees_balance']
doc_id1=money["doc_id"]

data1={'rupees_spent':rupees_spent,'rupees_balance':rupees_balance,'doc_id':doc_id1}

ref1 = db.collection("ProfileTest").document(doc_id).collection("ChaintanyaCurrency").document('fix').collection("Rupees").document()
ref1.set(data1)