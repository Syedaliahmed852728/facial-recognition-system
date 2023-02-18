import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionrealtime-40d84-default-rtdb.firebaseio.com/"
})


ref=db.reference('students')
data={
    "4308":{
        "Name": "Syed Ali Ahmed",
        "Major" : "software engineer",
        "Starting_Year" : 2021,
        "total_attendance":0,
        "Standing":'G',
        "Last_attendace_Time":"2022-12-11  00:54:34"
    },
    "4304": {
        "Name": "Muhammad Danyal",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4313": {
        "Name": "Abuzar Hassan",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4306": {
        "Name": "Adnan Mujahid",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4307": {
        "Name": "Muhammad Hammdullah",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4327": {
        "Name": "Sardar Munaqib",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4339": {
        "Name": "Anees-ur-rehman",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4349": {
        "Name": "Muhammd Salman",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4358": {
        "Name": "Usama Umer",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4363": {
        "Name": "khalid khan",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4350": {
        "Name": "Aryan Zaheer",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
       },
    "4345": {
        "Name": "Muhammad Sharjeel",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "4333": {
        "Name": "Siam Khan",
        "Major": "software engineer",
        "Starting_Year": 2021,
        "total_attendance": 0,
        "Standing": 'G',
        "Last_attendace_Time": "2022-12-11  00:54:34"
    }

}

for key,value in data.items():
    ref.child(key).set(value)
print("done...")
