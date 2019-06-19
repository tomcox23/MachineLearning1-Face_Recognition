import cv2
import os
#import GUI

path = os.path.dirname(os.path.abspath(__file__))
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier(path+r'\Classifiers\face.xml')
i=0
offset=50
name= "2" #name needs to be a number ie a student id number
os.mkdir("dataSetFolders/"+name) # make directory dataSetFolders/

while True:
	ret, im =cam.read()  # Read the video frame
	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # Convert the captured frame into grayscale
	faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE) # Get all faces from the video frame
	cv2.imshow('im',im)
	
	#take 21 images of a persons face and save images
	for(x,y,w,h) in faces:
		i=i+1
		cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset]) #save images to dataset folder for the trainer script to access
		cv2.imwrite("dataSetFolders/"+name+"/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset]) # save images to individual folders for each person, this is for image backups 
		cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
		cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
		cv2.waitKey(100)
		if i>20:
			cam.release()
			cv2.destroyAllWindows()
		break

