import cv2
import sys 


#cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
	ret,frame = video_capture.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
	
	#Draw ractangle around face
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
		
	#display image frame 
	cv2.imshow('Camera',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
		
#when everything done then 
video_capture.release()
cv2.distroyAllWindows()
