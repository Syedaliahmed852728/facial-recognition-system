import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionrealtime-40d84-default-rtdb.firebaseio.com/",
    'storageBucket':'facerecognitionrealtime-40d84.appspot.com'

})

# importing the student images
folderimagesPath='image'
modePathList=os.listdir(folderimagesPath)
imageList=[]
studentIds=[]
for path in modePathList:
    imageList.append(cv2.imread(os.path.join(folderimagesPath,path)))
    os.path.splitext(path)
    studentIds.append(os.path.splitext(path)[0])
    fileName=f'{folderimagesPath}/{path}'
    bucket=storage.bucket()
    blob=bucket.blob(fileName)
    blob.upload_from_filename(fileName)

def find_encoding(imagesList):
    encodeList=[]
    for img in imagesList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("encoding started....")
encodeListKnown=find_encoding(imageList)
encodingListKnownWithIds=[encodeListKnown,studentIds]
print("encoding completed")

file=open("encodeFile.p",'wb')
pickle.dump(encodingListKnownWithIds,file)
file.close()
print("File Saved")

# print(len(imageList))