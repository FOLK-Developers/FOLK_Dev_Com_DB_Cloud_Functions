
import time
import firebase_admin
from firebase_admin import firestore
import flask
from flask import request, jsonify
from firebase_admin import auth

# from firebase_admin import credentials
# cred = credentials.Certificate('../folk-bf69e-firebase-adminsdk-3bcpx-173db28c66.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()


firebase_admin.initialize_app()
db = firestore.client()




def getProfileFlags(url,domain):
    ProfileCol=None
    url_p=None
    if domain=="phone":
        url = url.strip()
        if url.startswith("+91") or url.startswith("91"):
            url_p = url[-10:]
        else:
            url_p=url
        ProfileCol = db.collection('Profile').where("mobile",'==',url_p)
    elif domain=='google.com':
        ProfileCol = db.collection('Profile').where("email",'==',url)
    
    preprimary_infostatus1=False
    ProfileDocExistsStatus1=False
    for pDoc in ProfileCol.stream():
        ldoc_id=pDoc.id
        ProfileDocExistsStatus1=True
        data = pDoc.to_dict()
        
        if 'flags' in data.keys():
            if 'pre_primary_info' in data['flags']:
                preprimary_infostatus1 = data['flags']['pre_primary_info']
            if 'primary_info' in data['flags']:
                 preprimary_infostatus1= data['flags']['primary_info']

    return {"preprimary_infostatus": preprimary_infostatus1, "profile_exist":ProfileDocExistsStatus1,"ldoc_id":ldoc_id}

def hello_world(request):
    recData = flask.request.json

    url_p=None
    uid="None"
    verification_status="Pending"
    print(recData)

    ProfileDocExistsStatus=False
    domain = recData['domain']
    url = recData['url']

    ldoc_id = ""
    vstatus = ""
    type = ""
    lpvstatus = False
    json_data=None

    if domain == 'phone' or domain == 'google.com':
        type = "communication"
    elif domain == 'facebook' or domain == 'github' or domain == 'linkedin':
        type = "social"

    docref = db.collection(u'LinkedProfiles') \
        .where(u'domain', u'==', domain) \
        .where('url', '==', url)
    docs = docref.stream()

    json_data=getProfileFlags(url,domain)



# If the Linked Profile is there and is verified then simply setting lpvstatus=True and returning
    for doc in docs:
        ldoc_id = doc.to_dict()['user_doc_id']
        vstatus = doc.to_dict()['verification_status']
    
    # preprimary_infostatus = False

    if ldoc_id != "":
        if vstatus == "Verified":
            lpvstatus = True

# If LinkedProfile is not there
    else:
                        
        if domain=='phone':
            modified_url=url
            try:
                user = auth.get_user_by_phone_number(modified_url)
                print(user.uid)
                vstatus='Verified'
                uid=user.uid
            except:
                print("Phone number not there!")
        elif domain=='google.com':
            try:
                user = auth.get_user_by_email(url)
                print(user.uid)
                vstatus='Verified'
                uid=user.uid
            except:
                print("Email not there!")




        # If profile does not exist then create it
        ProfileDocExistsStatus=json_data["profile_exist"]
        if ProfileDocExistsStatus ==False:
            dat={}
            if domain=='phone':
                dat={
                     "source":recData['source'],
                    "time_stamps":{"origin":int(time.time())},
                    "mobile":url
                }
            else:
                dat={
                    "time_stamps":{"origin":int(time.time())},
                     "source":recData['source'],
                    "email":url
                }
            docref = db.collection('Profile').document()
            docref.set(
                dat
            ,merge=True)

            print("Creating Profile")

            ldoc_id = docref.id


    #Creating the Linked Profile

        data = {
            "username":"Unknown",
            'verification_status':verification_status ,
            'verified_by': "None",
            'verified_timestamp': int(time.time()),  # Setting current by default
            'uid': uid,
            'type': type,
            'update_timestamp': int(time.time()),  # Setting current by default
            'user_doc_id': json_data["ldoc_id"],
            'domain': domain,
            'url': url,
            "source":recData['source']
        }
        docref = db.collection('LinkedProfiles').document()
        docref.set(data)
        print("Creating Linked profile")



    response = {
        "verification_status": lpvstatus,
        "preprimary_infostatus": json_data["preprimary_infostatus"],
        "user_doc_id":  json_data["ldoc_id"],
    }

    data = {
        'visibility_to_user': "Hidden",
        'activity_type': "Login",
        'category': "LinkedProfile",
        'sub_category': "linkedProfileExists",
        'details': domain,
        'sub_details': url,
        'performer': "user",
        'edate': int(time.time()),
        'doc_id':  json_data["ldoc_id"],
        'readable_date': firestore.SERVER_TIMESTAMP,
        'access_permission': ['admin']
    }

    docref = db.collection('Profile').document( json_data["ldoc_id"]).collection('activities').document()
    docref.set(data)

    print(response)

    return jsonify(response)







# hello_world({"source":
#     {"Zone":"VCM","Location":"Temple Desk","Campaign":"yoga_for_happiness","Referrer":"cGHgvv85qrbe16RDohXk","Medium":"whatsapp"},
#     "url":"shikharag.sa2002@gmail.com",
#     "domain":"google.com"
#     })


# recData = {'source':
#                {
#                 "Zone": "VCM",
#                 "Location":"Temple Desk",
#                 "Campaign":"yoga_for_happiness",
#                 "Referrer":"cGHgvv85qrbe16RDohXk",
#                 "Medium":"whatsapp"
#                 },
#            'url': "sahilsaini123@gmail.com",
#            'domain': "google.com"
# }

# recData = {'source':
#                {
#                 "Zone": "VCM",
#                 "Location":"Temple Desk",
#                 "Campaign":"yoga_for_happiness",
#                 "Referrer":"cGHgvv85qrbe16RDohXk",
#                 "Medium":"whatsapp"
#                 },
#            'url': "968266365x",
#            'domain': "phone"
# }





# hello_world(recData)



# Three cases:
#     profile exists:
#             linked profile does not exist
#             linked profile exists
#     Profile does not exist



