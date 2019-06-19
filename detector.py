import cv2,os
import numpy as np
from PIL import Image 

path = os.path.dirname(os.path.abspath(__file__))

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Load the trained mode
recognizer.read(path+r'\trainer\trainer.yml')
# Load prebuilt model for Frontal Face
cascadePath = path+"\\Classifiers\\face.xml"
# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Set the font style
fontFace = cv2.FONT_HERSHEY_SIMPLEX  #Creates a font
fontScale = 1 
fontColor = (255, 255, 255)

while True:

	ret, im =cam.read()    # Read the video frame
	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)     # Convert the captured frame into grayscale
	faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE) # Get all faces from the video frame
	
	# For each face in faces
	for(x,y,w,h) in faces:
		nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])  # Recognize the face belongs to which Name ID
		cv2.rectangle(im,(x-50,y-85),(x+w+50,y+h+50),(225,0,0),1) # Create rectangle around the face
		 # Check the if ID exist 
		if(nbr_predicted==1): # ==1 is refernce to image set 1
			nbr_predicted='Tom' # set the actual name to be displayed in the video stream
		elif(nbr_predicted==2):
			nbr_predicted='Joshua'
		elif(nbr_predicted==3):
			nbr_predicted='Sione'
		elif(nbr_predicted==4):
			nbr_predicted='David'
		elif(nbr_predicted==5):
			nbr_predicted='Laura'
		elif(nbr_predicted==6):
			nbr_predicted='Corey'
		elif(nbr_predicted==7):
			nbr_predicted='Sam'
		elif(nbr_predicted==8):
			nbr_predicted='Joe'
		elif(nbr_predicted==9):
			nbr_predicted='Adon'		
		else:
			nbr_predicted='Unknown'
		
	cv2.putText(im,str(nbr_predicted)+str(''), (x+50,y+h+30),fontFace, 1.1, (0,255,0)) #Draw the text Saying who is in the video
	cv2.imshow('im',im)

	# If 'q' is pressed, close program
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break
		
# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()