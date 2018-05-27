import os
import time
from Tkinter import *

def led_on():
	control_window.destroy()
	os.system("python device_controller.py")

control_window=Tk()

lab0=Label(text="Hello All! Welcome to the project.")
lab1=Label(text="To Start click START button")
lab2=Label(text="				")

btn1=Button(control_window,text='START',command=led_on)

lab0.pack()
lab1.pack()
lab2.pack()
btn1.pack()

w = 400 # width for the Tk root
h = 300 # height for the Tk root

# get screen width and height
ws = control_window.winfo_screenwidth() # width of the screen
hs = control_window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
control_window.geometry('%dx%d+%d+%d' % (w, h, x, y))


#control_window.geometry('{}x{}'.format(400, 300))
control_window.title("Start Project")
control_window.mainloop()
