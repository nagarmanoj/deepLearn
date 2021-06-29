import cv2 
import sys 



img = cv2.imread('Photos/rasmika.jpg')
cv2.imshow('Persion',img) 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Persion',gray)

haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print('Number of face found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2) 
	
cv2.imshow('Detected Face',img)

cv2.waitKey(0)
