import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

#Name = "6"

def addFace():
	os.system('python dataSetGenerator.py')
btn = Button(window, text="Add Face", bg="black", fg="white",command=addFace)
btn.grid(column=0, row=0, padx= 40, pady=50)

def train():
	os.system('python trainer.py')
btn2 = Button(window, text="Train", bg="black", fg="white",command=train)
btn2.grid(column=1, row=0, padx= 40)

def detector():
	os.system('python detector.py')
btn3 = Button(window, text="Detect", bg="black", fg="white",command=detector)
btn3.grid(column=2, row=0, padx= 40)

def Exit():
	quit()
btn3 = Button(window, text="Exit", bg="black", fg="white",command=Exit)
btn3.grid(column=4, row=0, padx= 40)

def setName():
	Name = txt.get()
	lbl.configure(text= Name)
btn3 = Button(window, text="Set Name", bg="black", fg="white",command=setName)
btn3.grid(column=2, row=2)

txt = Entry(window,width=15)
txt.grid(column=1, row=2)

lbl = Label(window, text="Name Variable")
lbl.grid(column=1, row=1)

window.mainloop()
