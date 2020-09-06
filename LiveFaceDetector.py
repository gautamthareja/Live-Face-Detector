import cv2

video = cv2.VideoCapture(0)
i=0
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True :
	check, frame = video.read()
	#print(check)
	#cv2.imshow('capturing', frame)
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05,minNeighbors=5)
	for x,y,w,h in faces:
		frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
	cv2.imshow('capturing', frame)
	key = cv2.waitKey(1)
	if key == ord(' '):
		break

cv2.destroyAllWindows
video.release()