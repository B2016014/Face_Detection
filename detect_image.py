#Face detection in an image
import cv2
#using a pre-trained model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read the input image as a gray scale image
img = cv2.imread('test.jpeg',0)
#To detect the faces----returns a list of rectangle coordinates
faces = face_cascade.detectMultiScale(img, 1.2, 5)
#making a rectangle  in detected face
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#showing the detected image
cv2.imshow('detected_image',img)
#holding the output window till Enter key is pressed
cv2.waitKey(0)
#closing all the windows
cv2.destroyAllWindows()
