import sys
import cv2
import os
import numpy as np
from PIL import Image 
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

def addFace():
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
            
#create Button + parameters, reference to def addFace
btn = Button(window, text="Add Face", bg="black", fg="white",command=addFace)
btn.grid(column=0, row=0, padx= 40, pady=50)

def train():
    path = os.path.dirname(os.path.abspath(__file__))
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cascadePath = path+r"\Classifiers\face.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    dataPath = path+r'\dataSet'
    #dataPath = path+r"/dataSet/"+name

    def get_images_and_labels(datapath):
        image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
        # images will contains face images
        images = []
        # labels will contains the label that is assigned to the image
        labels = []
        for image_path in image_paths:
            # Read the image and convert to grayscale
            image_pil = Image.open(image_path).convert('L')
            # Convert the image format into numpy array
            image = np.array(image_pil, 'uint8')
            # Get the label of the image
            nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
            #nbr=int(''.join(str(ord(c)) for c in nbr))
            print(nbr)
            # Detect the face in the image
            faces = faceCascade.detectMultiScale(image)
            # If face is detected, append the face to images and the label to labels
            for (x, y, w, h) in faces:
                images.append(image[y: y + h, x: x + w])
                labels.append(nbr)
                cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                cv2.waitKey(10)
        # return the images list and labels list
        return images, labels
    images, labels = get_images_and_labels(dataPath)
    cv2.imshow('test',images[0])
    cv2.waitKey(1)

    recognizer.train(images, np.array(labels))
    recognizer.save(path+r'\trainer\trainer.yml')
    cv2.destroyAllWindows()
	
	#create Button + parameters, reference to def train 
btn2 = Button(window, text="Train", bg="black", fg="white",command=train)
btn2.grid(column=1, row=0, padx= 40)

# Tell setector button to run detector.py script on click
def detector():
	os.system('python detector.py')
	
	#create Button + parameters, reference to def detector
btn3 = Button(window, text="Detect", bg="black", fg="white",command=detector)
btn3.grid(column=2, row=0, padx= 40)

# tell exit button to quit GUI on click
def Exit():
	quit()
	
	#create Button + parameters, reference to def Exit 
btn3 = Button(window, text="Exit", bg="black", fg="white",command=Exit)
btn3.grid(column=4, row=0, padx= 40)

def setName():
	Name = txt.get()
	lbl.configure(text= Name)
	
	#create Button + parameters, reference to def setName 
btn3 = Button(window, text="Set Name", bg="black", fg="white",command=setName)
btn3.grid(column=2, row=2)

#create set name text box
txt = Entry(window,width=15)
txt.grid(column=1, row=2)

lbl = Label(window, text="Name Variable")
lbl.grid(column=1, row=1)

window.mainloop()
