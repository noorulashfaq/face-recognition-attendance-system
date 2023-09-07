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
    'databaseURL':"https://faceattendancerealtime-7ce79-default-rtdb.firebaseio.com/",
    'storageBucket':"faceattendancerealtime-7ce79.appspot.com"
})

# Importing the student images into a list
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
# print(modePathList)
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path)
    # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket=storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)



print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("Encoding started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnown)
print("Encoding completed")

file = open("EncodeFile1.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")
