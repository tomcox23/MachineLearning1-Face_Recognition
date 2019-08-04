import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

#Tell add face button to run dataSetGenerator.py script on click
def addFace():
	os.system('python dataSetGenerator.py')
	
	#create Button + parameters, reference to def addFace
btn = Button(window, text="Add Face", bg="black", fg="white",command=addFace)
btn.grid(column=0, row=0, padx= 40, pady=50)

# Tell train button to run trainer.py script on click
def train():
	os.system('python trainer.py')
	
	#create Button + parameters, reference to def train 
btn2 = Button(window, text="Train", bg="black", fg="white",command=train)
btn2.grid(column=1, row=0, padx= 40)

# Tell detector button to run detector.py script on click
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
	
	#create set name text box
txt = Entry(window,width=15)
txt.grid(column=1, row=2)

lbl = Label(window, text="Name")
lbl.grid(column=1, row=1)

	#create Button + parameters, reference to def setName 
btn3 = Button(window, text="Set Name", bg="black", fg="white",command=setName)
btn3.grid(column=2, row=2)
	

def setID():
	ID = txtID.get()
	lbl.configure(text= ID)
	
#create set ID text box
txt2 = Entry(window,width=15)
txt2.grid(column=1, row=6)

lbl2 = Label(window, text="ID")
lbl2.grid(column=1, row=4)

	#create Button + parameters, reference to def setName 
btn4 = Button(window, text=" Set ID ", bg="black", fg="white",command=setName)
btn4.grid(column=2, row=6)

window.mainloop()
