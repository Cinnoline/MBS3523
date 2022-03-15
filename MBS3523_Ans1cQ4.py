import cv2
import numpy as np
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
    cv2.putText(imgGray, 'MBS3523 Assignment 1c - Q4     Name: ZHANG Jianru', (20, 50), font, 0.6, (255, 255, 0), 2)
    for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
       imgcrop = img[y:(y+h), x:(x+w)]
       imgGray[y:(y+h), x:(x+w)] = imgcrop

       cv2.imshow('img', imgGray)

    if cv2.waitKey(5) & 0xff == 27:
        break

capture.release()
cv2.destroyAllWindows()