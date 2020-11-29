
import firebase_admin
from firebase_admin import credentials, firestore
from flask import jsonify

cred = credentials.Certificate('folk-dev-com-db-firebase-adminsdk-mz02x-6bcb0d65ae.json')

firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': 'https://folk-database.firebaseio.com/'
                              })

db =firestore.client()

recdata={
    "evaluation": "val",
    "doc_id": "val",
    "evaluated_by": "val",
    "name_of_skill": "val"
}



def hello_world(request):
    # recdata = flask.request.json
    print("Received Data :", recdata)


    evaluation = recdata['evaluation']
    doc_id=recdata['doc_id']
    evaluated_by = recdata['evaluated_by']
    name_of_skill = recdata['name_of_skill']

    ref = db.collection("Profile").document(doc_id).collection("Skills").document()

    data = {
        "evaluation": evaluation,
        "doc_id": doc_id,
        "evaluated_by": evaluated_by,
        "name_of_skill": name_of_skill
    }

    ref.set(data)

    response = {
        "status": "True",
        "message": "Skill added successfully!"
    }

    return jsonify(response)
