## How To Use
all commands run using the anaconda terminal. run by typing <code>python guiV2.py</code> to run the user interface for example.

### GUI
* To use the GUI run <code>python guiV2.py</code> you will be able to run each script from in the GUI as well.

![GUI Layout](/readmeImages/main.PNG)

#### First 

* Add a name to the Name text Box
* make sure you are the only person infront of the camera
* Make sure you are not too close or far away from the camera and look directly at it.
* Click add Face Button. this wll take 21 images of your face.

![image window](/readmeImages/mainAddperson.PNG)

![console output](/readmeImages/addimages.png)

![console output](/readmeImages/AddfaceConsole.PNG)

* The console will display the new list of people added and if the photos were successful
#### Second
* Click the Train Button. 

![console output](/readmeImages/mainTrain.png)

#### Third
* Click detect
* This will bring up the camera window identifying whoever is in the frame
* Push "Q" button to exit the camera window and go back to the GUI.

![Detect window and GUI](/readmeImages/detvideo.PNG)

#### Forth 
* Click Exit button to exit the program

### Delete Users
* click user list button

![userlist](/readmeImages/mainUser.PNG)

![userlist](/readmeImages/mainDele.PNG)

* click on user you want to delete

![userlist](/readmeImages/userdel.PNG)

![userlist](/readmeImages/delmes.PNG)

### SEND DATA TO SERVER

#### First 
* start server program with <code>python Server.py</code>
#### Second 

![server window](/readmeImages/server.PNG)

* push start server button. 
**this sets up the server ready for connection 

![Server Start](/readmeImages/serverStart.PNG)

* Back in the main program push the DETECT button
** this connects to the server and will stream data. ie who is in the video stream

![detect](/readmeImages/mainDetec.PNG)

* Push Q to quit the video stream in the main application.
** this will shut off the server

![detect](/readmeImages/serverOut.PNG)
