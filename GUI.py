import sys
import cv2
import os
import shutil
import numpy as np
import PIL.Image 
from tkinter import *
import json

window=Tk()

window.title("Running Python Script")
window.geometry('550x250')


user_dict = {

}


try:
    with open('users.json', 'r') as f:
        user_dict = json.loads(f.read())
    
except:
    print("An exception occurred")          
     
     
def addFace():

    name = txt_name.get()
    id_number = len(user_dict.keys()) + 1
    print("id number at start ",id_number)
    path = os.path.dirname(os.path.abspath(__file__))
    cam = cv2.VideoCapture(cv2.CAP_DSHOW)
    detector=cv2.CascadeClassifier(path+r'\Classifiers\face.xml')
    i=0
    offset=50
    
    try:
        os.mkdir("dataSetFolders/"+str(id_number)) # make directory dataSetFolders/
        print("id number mkdir",id_number)
    except:
        print("dataSetFolder already exists error")
        print("id number mkdir except ",id_number)
        
    user_dict[str(id_number)] = name
        
    j = json.dumps(user_dict) # j is now a string containing the data from dict in the json format.
    with open('users.json', 'w') as f:
        f.write(j)
    
    print(user_dict)

    
    try:
        while True:
            
            
            ret, im=cam.read()  # Read the video frame
            #take 21 images of a persons face and save images
            if(im is not None):
                gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # Convert the captured frame into grayscale
                faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE) # Get all faces from the video frame
                cv2.imshow('im',im)
                
                for(x,y,w,h) in faces:
                    i+=1
                    cv2.imwrite("dataSet/face-"+str(id_number) +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset]) #save images to dataset folder for the trainer script to access
                    cv2.imwrite("dataSetFolders/"+str(id_number)+"/face-"+str(id_number) +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset]) # save images to individual folders for each person, this is for image backups 
                    cv2.rectangle(im,(x-offset,y-offset),(x+w+offset,y+h+offset),(225,0,0),2)
                    cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
                    cv2.waitKey(100)
                
                    if i>20:
                        cam.release()
                        cv2.destroyWindow('im')
                        print("Successfully taken photos set id number is ",id_number)
                        id_number += 1
                        

                    break
                    

            else:  
                break
    except:  
        print("An error occurred. Try moving your face back from the camera")
        shutil.rmtree("dataSetFolders/"+str(id_number)) # removes directory dataSetFolders/
        del user_dict[str(id_number)]
        print(user_dict)
        #print("Face too close id number ",id_number)
        
        
#create Button + parameters, reference to def addFace
btn_add_face = Button(window, text="Add Face", bg="black", fg="white",command=lambda: addFace())
btn_add_face.grid(column=0, row=0, padx= 40, pady=50)


def train():
    path = os.path.dirname(os.path.abspath(__file__))
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cascadePath = path+r"\Classifiers\face.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    dataPath = path+r'\dataSet'

    
    def get_images_and_labels(datapath):
        image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
        # images will contains face images
        images = []
        # labels will contains the label that is assigned to the image
        labels = []
        for image_path in image_paths:
            # Read the image and convert to grayscale
            image_pil = PIL.Image.open(image_path).convert('L')
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
    cv2.imshow('Training...',images[0])
    cv2.waitKey(1)

    recognizer.train(images, np.array(labels))
    recognizer.save(path+r'\trainer\trainer.yml')
    cv2.destroyAllWindows()
	
	#create Button + parameters, reference to def train 
btn_train = Button(window, text="Train", bg="black", fg="white",command=train)
btn_train.grid(column=1, row=0, padx= 40)


# Tell detector button to run detector.py script on click
def detector():
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
    cam = cv2.VideoCapture(cv2.CAP_DSHOW)

    # Set the font style
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  #Creates a font
    fontScale = 1 
    fontColor = (255, 255, 255)
    
    try:
        while True:
    
            ret, im =cam.read()    # Read the video frame
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)     # Convert the captured frame into grayscale
            faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE) # Get all faces from the video frame
            
            # For each face in faces
            for(x,y,w,h) in faces:
                nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])  # Recognize the face belongs to which id_number
                cv2.rectangle(im,(x-50,y-85),(x+w+50,y+h+50),(225,0,0),1) # Create rectangle around the face
                
                if str(nbr_predicted) in user_dict:
                    nbr_predicted = user_dict[str(nbr_predicted)]
                else:
                    nbr_predicted = "unknown"
                # Check the if ID exist 
                
            cv2.putText(im,str(nbr_predicted)+str(''), (x+50,y+h+30),fontFace, 1.1, (0,255,0)) #Draw the text Saying who is in the video
            cv2.imshow('Face Detector',im)
    
            # If 'q' is pressed, close window
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break
            
        # Stop the camera
        cam.release()
    
        # Close all windows
        cv2.destroyAllWindows()
        
    except:
        print("No faces detected in frame.")
        print("Make sure you are infront of the camera")
        
#create Button + parameters, reference to def detector
btn_detect = Button(window, text="Detect", bg="black", fg="white",command=detector)
btn_detect.grid(column=2, row=0, padx= 40)

def deleteUser():

    lbt=ListUserBox()
        
        
# tell exit button to quit GUI on click
def Exit():
    quit()
	
	#create Button + parameters, reference to def Exit 
btn_exit = Button(window, text="Exit", bg="black", fg="white",command=Exit)
btn_exit.grid(column=4, row=0, padx= 40)

#create set name text box
lbl_name = Label(window, text="Name")
lbl_name.grid(column=0, row=1)
txt_name = Entry(window,width=15)
txt_name.grid(column=1, row=1)

#user list button
btn_deleteUser = Button(window, text="User List", bg="black", fg="white",command=deleteUser)
btn_deleteUser.grid(column=0, row=10, padx= 40)


class ListUserBox :
    def __init__(self) :
        self.root = Tk()
        self.list_box_1 = Listbox(self.root, width = 50, selectmode=EXTENDED)
        self.list_box_1.pack(fill = BOTH, expand=True)
        self.delete_button = Button(self.root, text="Delete",command=self.DeleteSelection)
        self.delete_button.pack()
        
        
        for key in sorted(user_dict):
            self.list_box_1.insert(END, '{}: {}'.format(key, user_dict[key]))

    def DeleteSelection(self) :
        items = self.list_box_1.curselection()
        pos = 0
        for i in items :
            id_number = self.list_box_1.get(i)
            idx = int(i) - pos
            self.list_box_1.delete( idx,idx )
            pos = pos + 1
            
            text = str(id_number)
            sep = ':'
            rest = text.split(sep, 1)[0]
        
            try:
                print(id_number + " has been deleted")
                #print(int(rest))
                del user_dict[str(rest)]
                j = json.dumps(user_dict) # j is now a string containing the data from dict in the json format.
                with open('users.json', 'w') as f:
                    f.write(j)
                print(user_dict)
                shutil.rmtree("dataSetFolders/"+str(rest))
                f=0
                while f < 21:
                    f += 1
                    os.remove("dataSet/face-"+str(rest) +'.'+ str(f) + ".jpg")
                    
                break
            except KeyError:
                print("Key not found")
            


window.mainloop()

