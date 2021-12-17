#Face detection
import cv2
#using a pre-trained model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read the input image
img = cv2.imread('test.jpeg')
#Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#making a rectangle frame in detecting the face
for (x,y,w,h) in faces:
    cv2.rect angle(img,(x,y),(x+w,y+h),(255,0,0),2)
#showing the detected image
cv2.imshow('img',img)
#holding the output window till enter key is pressed
cv2.waitKey(0)
