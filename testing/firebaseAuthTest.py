import firebase_admin
from firebase_admin import firestore

firebase_admin.initialize_app()

count = None
db = firestore.client()


def hello_auth(event, context):
    """Triggered by a change to a Firebase Auth user object.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    # The unique id of the user whose auth record changed
    uid = event['uid']
    # print out the uid that caused the function to be triggered
    print(f"Function triggered by change to user: {uid}.")
    # now print out the entire event object
    print(event)
    print('Firebase Auth event: ', str(event))
