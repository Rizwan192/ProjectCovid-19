import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('facial features.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_id = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").capitalize()
            #print(label, path)
            if not label in label_id:
                label_id[label] = current_id
                current_id += 1
            id_ = label_id[label]
            #print(label_id)
            #y_labels.append(label)
            #x_train.append(path)

            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")
            #print(image_array)

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=8)

            for(x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

#print(y_labels)
#print(x_train)

with open("labels.pkl", 'wb') as f:
    pickle.dump(label_id, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")