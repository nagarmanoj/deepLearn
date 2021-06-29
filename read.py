import cv2 as cv 
#img = cv.imread("Photos/rasmika.jpg")
#cv.imshow('Rasmika',img)
#cv.waitKey(0)

# Reading video

capture = cv.VideoCapture('Videos/Kaka WRLD - Bholenath (A Love Story) - Official Video - Arvindr Khaira - Main Bhola Parvat Ka.webm')
while True:
	isTrue,frame = capture.read()
	cv.imshow('Video',frame)
	
	if cv.waitKey(20) & 0xFF==ord('d'):
		break 
		
capture.release()
cv.distroyAllWindows()
