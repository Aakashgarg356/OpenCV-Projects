import numpy as np
import cv2 as cv

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
face_classifier = cv.CascadeClassifier(
                "C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Recognition\\face_classifier.xml")

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy', allow_pickle=True)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("faces_trained.yml")
img = cv.imread(r'C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Recognition\\Faces\\val\\madonna\\4.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
detect = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
for (x, y, w, h) in detect:
        faces_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(faces_roi)
        if confidence>100:
                print("This image is not producing correct label..")
        else:
                print(f"Label = {people[label]} with a confidence of {confidence}")

        cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow("Detected Face", img)
cv.waitKey(0)
cv.destroyAllWindows()