import labels as labels
import numpy as np
import cv2
import pickle
from datetime import datetime
import threading
import time
from firebase import firebase
cap = cv2.VideoCapture(0)
CameraId='123'
p_name= ''
p_timestamp: ''
firebase = firebase.FirebaseApplication('https://stickynote-3a600.firebaseio.com/', None)
face_cascade = cv2.CascadeClassifier('facial features.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
#def delay():
    #threading.Timer(3.0, delay).start()
def printingOutput():
    time.sleep(1.5)
    if conf >= 45 and conf <= 80:
        with open('output.txt', 'a') as f:
            today = datetime.now()
            print(labels[id_], "Was here at camera ", cap, file=f)
           
            print(today, file=f)
            print(labels[id_], "Was here at camera ", cap)
            print(today)
            p_name= labels[id_]
            p_timestamp=today
            camera=cap
            data = {
                'p_name': p_name,
                'p_timestamp': today,

            }
            result = firebase.post('/stickynote-3a600/Live_Tracking',data)


    else:
        print("unknown")

#today = datetime.now()

labels = {"person_name": 1}
with open("labels.pkl", 'rb') as f:
    original_labels = pickle.load(f)
    labels = {v: k for k, v in original_labels.items()}

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=8)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 1)
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        id_, conf = recognizer.predict(roi_gray)

        x = threading.Thread(target=printingOutput(), args=(1,))
        x.start()   #Running the recognizer confidence check via THREADING


    cv2.imshow('mat', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
