import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-7ce79-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "21CS156":
        {
            "name" : "Srimathi",
            "major": "CSE",
            "year": 3,
            "starting year":"2021",
            "total_attendance": 13,
            "last_attendance_time":"2023-09-05 00:54:34"

        },
    "21CS145":
        {
            "name": "Sasi",
            "major": "CSE",
            "year": 3,
            "starting year":"2021",
            "total_attendance": 10,
            "last_attendance_time":"2023-09-05 00:54:34"
        },
    "21CS154":
        {
            "name": "Sridharshini",
            "major": "CSE",
            "year": 3,
            "starting year":"2021",
            "total_attendance": 12,
            "last_attendance_time":"2023-09-05 00:54:34"
        },
    "21CS124":
        {
            "name": "Noorul Ashfaq",
            "major": "CSE",
            "year": 3,
            "starting year":"2021",
            "total_attendance": 9,
            "last_attendance_time":"2023-09-05 00:54:34"
        }


}

for key,value in data.items():
    ref.child(key).set(value)