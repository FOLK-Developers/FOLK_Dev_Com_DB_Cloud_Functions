from pyrebase import pyrebase
from getpass import getpass

firebaseConfig = {
    # Firebase project app config here.
    # FireBase Project->Settings->General->Firebase SDK snippet(config)->copy->paste here and format as a dictionary
    #"apiKey": "your_api_key_here", #and so on...
    "authDomain": "testproject1-11f00.firebaseapp.com",
    "databaseURL": "https://testproject1-11f00.firebaseio.com",
    "projectId": "testproject1-11f00",
    "storageBucket": "testproject1-11f00.appspot.com",
    "messagingSenderId": "160341011612",
    "appId": "1:160341011612:web:d99d20e1b28265d92a5159",
    "measurementId": "G-6ME868742E"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


def signUp():
    email = input("Enter Email: \n")
    password = getpass("Enter password: \n")
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Signed up successfully\n")
        askUser = input("Want to login?[Y/N]")
        if askUser == 'y' or askUser == 'Y':
            login()
    except:
        print("User already exists!")


def login():
    email = input('Enter Email: ')
    password = getpass("Enter password: ")
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Logged in Successfully\n")
    except:
        print("Invalid Credentials!")


def resetPassword():
    email = input("Enter email: ")
    auth.send_password_reset_email(email)
    print("Link to reset password has been send to your registered email id\n")

print("Enter your option: ")
inp = int(input("1.- SignUp\n2.- Login\n3.- Reset Password\n"))

while inp!=1 and inp!=2 and inp!=3:
    print("Your input was invalid option!\n")
    inp = input("1.- SignUp\n2.- Login\n3.- Reset Password\n")

if inp == 1:
    signUp()
elif inp == 2:
    login()
else:
    resetPassword()

