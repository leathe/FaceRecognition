import numpy as np
import os
import cv2
# import imp

# print(imp.find_module("cv2"))
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('video.mp4')
rec = cv2.face.createLBPHFaceRecognizer()
rec.load('recognizer/trainingData.yml')
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 255), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        print(id)
        print(conf)
        if conf < 65:
            if id == 1:
                id = "Bill Gates"
        else:
            id = "Unknown"
        cv2.putText(img, str(id), (x, y+h), font, 1, (255, 0, 255), 2)
    cv2.imshow("Face", img)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
