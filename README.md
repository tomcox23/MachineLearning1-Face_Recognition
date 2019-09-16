## Installation. 

#### The current master comes In a pip enviroment so no manual installation of any libraries is needed

If you would still like to install everything manually then follow the following 
how to install in the anaconda terminal I used eg. <code>Pip install Numpy</code> or <code>conda Install Numpy</code>

* Python 3.6.4. ideally python 3.7 to get Tkinter to work for the GUI.
* OpenCV 3.4.1 
* opencv-contrib-python 4.0 This fixed cv2 no attribute errors
* Numpy
* Pillow
* Tkinter, should come with python 3.7

Folders that need to be created in the root working directory.

* Create an empty Folder named **"dataSet"** in the same directory where the python scripts are
* Create an empty Folder named **"dataSetFolders"** in the same directory
* Create an empty folder called **trainer** In same directory 

## How To Use
all commands run using the anaconda terminal. run by typing "python GUI.py" to run the user interface for example.

### GUI
* All scripts have been merged into the GUI.py script. The other seperate Scripts are now not used at all. "dataSetGenerator","trainer","detector"
* To use the GUI run <code>python GUI.py</code> you will be able to run each script from in the GUI as well.

#### First 
* Add a name to the Name text Box
#### Second
* make sure you are the only person infront of the camera
* Make sure you are not too close or far away from the camera and look directly at it.
* Click add Face Button. this wll take 21 images of your face.
#### Third
* Click the Train Button. 

#### Forth
* Click detect
* This will bring up the camera window identifying whoever is in the frame
* Push "Q" button to exit the camera window and go back to the GUI.
#### Fifth 
* Click Exit button to exit the program




## Old How To Use

### dataSetGenerator
* In dataSetGenerator.py change Name "" to eg Name "11". this will set the name for the users imgages and folders. it must be an integer though. Next you run python dataSetGenerator.py.
* Note, make sure the person you are taking a photo of is actually in the camera frame or it will error out if no face is being detected.

### trainer
* run python trainer.py.

### detector
 * The predictor number must be the same as the Name "11" in order to know who it is looiking at. ie predicting image set 11.
 * Run python detector.py

### Issue Fix

- no cv2 idendified = pip install opencv-python
