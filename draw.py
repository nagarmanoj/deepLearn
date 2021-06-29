import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#blank[200:300,300:400] = 0,0,255
#cv.imshow("Green",blank)

#img = cv.imread('Photos/rasmika.jpg')
#cv.imshow('Rasmika',img)


# draw the Rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('Ractangle',blank)

# draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('circle',blank)

#Draw a Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=1)
cv.imshow('Line',blank)

#wright Text

cv.putText(blank,'Hello,Manoj',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)


cv.waitKey(0)
