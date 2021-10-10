import cv2 as cv
from random import randrange

face_classifier = cv.CascadeClassifier(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Smile Detection App\face_classifier.xml")
smile_classifier = cv.CascadeClassifier(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Smile Detection App\smile.xml")

video = cv.VideoCapture(0)
while True:
    count, frame = video.read()
    if count:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    else:
        break
    face_coordinates = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 2)
    for (x, y, w, h) in face_coordinates:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 230), 2)
        the_faces = frame[y:y+h, x:x+w]
        gray = cv.cvtColor(the_faces, cv.COLOR_BGR2GRAY)
        smile_coordinates = smile_classifier.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 20)
        for (x, y, w, h) in smile_coordinates:
            cv.rectangle(the_faces, (x, y), (x+w, y+h), (25, 0, 0), 2)
        print(len(smile_coordinates))
        if len(smile_coordinates)>0:
            cv.putText(frame, 'smiling', (x+20, y+h+200), fontScale=3, fontFace=cv.FONT_HERSHEY_TRIPLEX, color=(randrange(0, 255), 200, 100))
    cv.imshow("Smile Detection App", frame)
    key = cv.waitKey(1)
    if key==81 or key==113:
        break
video.release()
cv.destroyAllWindows()