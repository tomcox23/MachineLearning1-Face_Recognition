#!/usr/bin/env python

import socket
from tkinter import *
 
window = Tk()
 
window.title("Easy Server")
window.geometry('300x200')
 
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

def basicServer():
    
    print("server Starting")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print('Connection address:', addr)
    while 1:
        try:
            data = conn.recv(BUFFER_SIZE).decode('utf-8')
            if not data: break
        except:
            print("no more messages")
            break
        lbl_data = Label(window, text=("received data:", data))
        lbl_data.grid(column=1, row=3)
        print("received data:", data)

        if data == "disconnect": break
    print("shut off server")
    
    try:
        sendData = "disconnected"
        conn.send(sendData.encode('utf-8'))
        conn.close()
    except:
        pass
def Exit():
    quit()


    
btn_exit = Button(window, text="Exit", bg="black", fg="white",command=Exit)
btn_exit.grid(column=3, row=1, padx= 40)

btn_exit = Button(window, text="Start server", bg="black", fg="white",command=basicServer)
btn_exit.grid(column=1, row=1, padx= 40)
    
window.mainloop()