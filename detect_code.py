#Face detection in an image
import cv2
#using a pre-trained model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read the input image
img = cv2.imread('test.jpeg')
#Convert into grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, 1.2, 5)
#making a rectangle frame in detecting the face
for (x,y,w,h) in faces:
    cv2.rect angle(img,(x,y),(x+w,y+h),(0,0,255),2)
#showing the detected image
cv2.imshow('detected_image',img)
#holding the output window till Enter key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
