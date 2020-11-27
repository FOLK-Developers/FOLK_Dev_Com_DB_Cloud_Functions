import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-20922898af.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://folk-database.firebaseio.com/'
})
# # token = []
db = firestore.client()




def getProfileFlags(doc_id):
    docref = db.collection('Profile').document(doc_id)
    data = docref.get().to_dict()
    print("getProfileFlags():",data)
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


getProfileFlags('x5zctb6WuKWVE5WjxhU2')

# prodata = db.collection('Profile').document('x5zctb6WuKWVE5WjxhU2')
