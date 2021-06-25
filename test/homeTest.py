import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('./../folk-dev-com-db-firebase-adminsdk-mz02x-20922898af.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://folk-database.firebaseio.com/'
}) 
# # token = [] 
db = firestore.client()      
 

