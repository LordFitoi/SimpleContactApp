import pyrebase
import os

config = {
    "apiKey": "AIzaSyAGXaipET0equJGgyYjeolM-fB_dUsAjIo",
    "authDomain": "simplecontact-e40cd.firebaseapp.com",
    "projectId": "simplecontact-e40cd",
    "storageBucket": "simplecontact-e40cd.appspot.com",
    "messagingSenderId": "198176417910",
    "appId": "1:198176417910:web:b09a831f6d3bfd8fc89757",
    "measurementId": "G-FP08ZN4T3Z",
    "databaseURL": "https://simplecontact-e40cd-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()