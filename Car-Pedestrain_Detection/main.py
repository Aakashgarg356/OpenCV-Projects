import cv2 as cv
from random import randrange

# Car and Pedestrain Detection in an Image
# car_classifier = cv.CascadeClassifier(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Car-Pedestrain_Detection\car.xml")
# full_body_classifier = cv.CascadeClassifier(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Car-Pedestrain_Detection\full_body.xml")
# img_file = r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Car-Pedestrain_Detection\last.jpg"
# img = cv.imread(img_file)
# cv.imshow("Original", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# car_coordinates = car_classifier.detectMultiScale(gray)
# print(car_coordinates)
# for (x, y, w, h) in car_coordinates:
#     cv.rectangle(img, (x, y), (x+w, y+h), (randrange(0, 255), randrange(0, 255), randrange(0, 255)))
# cv.imshow("Detected Image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Car and Pedestrain Detection in a video
# car_classifier = cv.CascadeClassifier(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Car-Pedestrain_Detection\car.xml")
# full_body_classifier = cv.CascadeClassifier(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Car-Pedestrain_Detection\full_body.xml")
# video = cv.VideoCapture(r"C:\Users\Aakash Garg\Documents\OpenCV-Projects\Car-Pedestrain_Detection\testcar.mp4")
# while True:
#     count, frame = video.read()
#     if count:
#         gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     else:
#         break
#     car_coordinates = car_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
#     full_body_coordinates = full_body_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
#     # print(car_coordinates)
#     for (x, y, w, h) in car_coordinates:
#         cv.rectangle(frame, (x+2, y+2), (x+w, y+h), (200, randrange(0, 255), 100))
#         cv.rectangle(frame, (x, y), (x+w, y+h), (0, randrange(0, 255), 2))
#     for (x, y, w, h) in full_body_coordinates:
#         cv.rectangle(frame, (x, y), (x+w, y+h), (212, 0, 233), 2)
#     cv.imshow("Original", frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# video.release()
# cv.destroyAllWindows()