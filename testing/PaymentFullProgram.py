
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
silver_coins_spent=['silver_coins_spent']
copper_coins_spent=['copper_coins_spent']
gold_coins_balance=['gold_coins_balance']
silver_coins_balance=['silver_coins_balance']
copper_coins_balance=['copper_coins_balance']
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


#PAYMENT


payment={'paid_chaintanya_coins':'0','paid_rupees':'0','paid_amount':'0','payment_method':'0','doc_id':'1','type':''}
paid_chaintanya_coins=payment['paid_chaintanya_coins']
paid_rupees=payment['paid_rupees']
paid_amount=payment['paid_amount']
payment_method=payment['payment_method']
doc_id2=payment['doc_id']
payment_type=payment['type']

data2={'type':payment_type,'paid_chaintanya_coins':paid_chaintanya_coins,'paid_rupees':paid_rupees,'time':int(time.time()),'paid_amount':paid_amount,'doc_id':doc_id2}

ref2 = db.collection("ProfileTest").document(doc_id).collection("PaymentsFeature").document()
ref2.set(data2)



#PRODUCT


products={'cost':'0','discounts':'0','image_link':'0','name':'','type':'','size':'0','doc_id':'1'}
cost=products['cost']
discount=products['discounts']
image_link=products['image_link']
name=products['name']
type=products['type']
size=products['size']
doc_id3=products['doc_id']

data3={'cost':cost,'discount':discount,'image_link':image_link,'name':name,'product_type':type,"size":size,'doc_id':doc_id3}

ref3 = db.collection("ProfileTest").document(doc_id).collection("ProductsFeature").document()
ref3.set(data3)


#REFERRAL

referral={'amount':'0','referral_name':'','referral_profile_id':'','referral_email_id':'','doc_id':'1'}
amount=referral['amount']
referral_name=referral['referral_name']
referral_profile_id=referral['referral_profile_id']
referral_email_id=referral['referral_email_id']
doc_id4=referral['doc_id']

data4={'amount':amount,'referral_name':referral_name,'referral_profile_id':referral_profile_id,'time':int(time.time()),'referral_email_id':referral_email_id,'doc_id':doc_id4}

ref4 = db.collection("ProfileTest").document(doc_id).collection("ReferralSchemeFeature").document()
ref4.set(data4)

