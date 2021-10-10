import os
import numpy as np
import cv2 as cv

# p = []
# for i in os.listdir("C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Recognition\\Faces\\train"):
#     p.append(i)
# print(p)
peoples = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

features = []
labels = []
dir = r"C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Recognition\\Faces\\train"

def create_train():
    for person in peoples:
        path = os.path.join(dir, person)
        label = peoples.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            face_classifier = cv.CascadeClassifier("C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Recognition\\face_classifier.xml")
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            detect = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
            for (x, y, w, h) in detect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
# print(len(features))
# print(len(labels))
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save("faces_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", labels)