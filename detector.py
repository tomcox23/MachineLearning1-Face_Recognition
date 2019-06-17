import cv2,os
import numpy as np
from PIL import Image 

path = os.path.dirname(os.path.abspath(__file__))

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(path+r'\trainer\trainer.yml')
cascadePath = path+"\\Classifiers\\face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)

fontFace = cv2.FONT_HERSHEY_SIMPLEX  #Creates a font
fontScale = 1
fontColor = (255, 255, 255)

while True:
	ret, im =cam.read()
	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
	for(x,y,w,h) in faces:
		nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
		cv2.rectangle(im,(x-50,y-85),(x+w+50,y+h+50),(225,0,0),1)
		if(nbr_predicted==1):
			nbr_predicted='Tom'
		elif(nbr_predicted==2):
			nbr_predicted='Joshua'
		elif(nbr_predicted==3):
			nbr_predicted='Sione'
		elif(nbr_predicted==4):
			nbr_predicted='David'
		elif(nbr_predicted==5):
			nbr_predicted='Laura'
			
		cv2.putText(im,str(nbr_predicted)+str(''), (x+50,y+h+30),fontFace, 1.1, (0,255,0)) #Draw the text
		cv2.imshow('im',im)
		cv2.waitKey(10)

