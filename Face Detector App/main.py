import cv2 as cv
from random import randrange

# Face Detection in an Image
# face_classifier = cv.CascadeClassifier("C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Detector App\\face_classifier.xml")
# img = cv.imread(r"C:\Users\Aakash Garg\Downloads\collage.jpg")
# resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//3), interpolation=cv.INTER_AREA)
# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# face_coordinates = face_classifier.detectMultiScale(gray)
# # (x, y, w, h) = face_coordinates[0]
# for (x, y, w, h) in face_coordinates:
#     cv.rectangle(resized, (x, y), (x+w, y+h), (randrange(0, 255), randrange(0, 255), randrange(0, 255)), 1)
# cv.imshow("Duplicate", resized)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Face Detection in a Video
# video = cv.VideoCapture(0)
video = cv.VideoCapture(0)
face_classifier = cv.CascadeClassifier("C:\\Users\\Aakash Garg\\Documents\\OpenCV-Projects\\Face Detector App\\face_classifier.xml")
while True:
    count, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_coordinates = face_classifier.detectMultiScale(gray)
    for (x, y, w, h) in face_coordinates:
        cv.rectangle(frame, (x, y), (x+w, y+h), (randrange(0, 255), randrange(0, 255), randrange(0, 255)), 3)
    cv.imshow("Face Detection", frame)
    # if cv.waitKey(1) & 0xFF==ord('q'):
    #     break
    key = cv.waitKey(1)
    if key==81 or key==113:
        break
video.release()
cv.destroyAllWindows()