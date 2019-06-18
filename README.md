### Installing
* how to install in the anaconda terminal I used eg. Pip install Numpy. or conda Install Numpy

* Python 3.6.4. ideally python 3.7 to get Tkinter to work for the GUI.
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

### trainer.py
* run python trainer.py.

### detector.py
* add new elif statement to the dector.py
		elif(nbr_predicted==11):
			nbr_predicted='Sam' 
 * The predictor number must be the same as the Name "11" in order to know who it is looiking at. ie predicting image set 11.
 * Run python detector.py

* To use the GUI run python GUI.py you will be able to run each script from in the GUI as well. 
