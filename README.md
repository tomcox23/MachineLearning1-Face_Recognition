### Installing
* how to install in the anaconda terminal I used eg. <code>Pip install Numpy</code> or <code>conda Install Numpy</code>

* Python 3.7
* OpenCV 3.4.1 
* opencv-contrib-python 4.0 This fixed cv2 no attribute errors
* Numpy
* Pillow
* Tkinter, should come with python 3.7

Folders that need to be created in the root working directory.

* Create an empty Folder named **"dataSet"** in the same directory where the python scripts are 
* Create an empty folder called **trainer** In same directory 

## Running Instructions 
all commands run using the anaconda terminal
### dataSetGenerator
* In dataSetGenerator.py change Name "" to eg Name "11". this will set the name for the users imgages and folders. it must be an integer though. Next you run python dataSetGenerator.py.
* Note, make sure the person you are taking a photo of is actually in the camera frame or it will error out if no face is being detected.

### trainer
* run python trainer.py.

### detector
* add new elif statement to the detector.py
		<code>elif(nbr_predicted==11):
			nbr_predicted='Sam'</code>
 * The predictor number must be the same as the Name "11" in order to know who it is looiking at. ie predicting image set 11.
 * Run python detector.py
 
### GUI
* To use the GUI run python GUI.py you will be able to run each script from in the GUI as well. 


### Issue Fix

- no cv2 idendified = pip install opencv-python