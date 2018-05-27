import serial
import os
import time
from Tkinter import *

def operateOn():
	arduinoData.write('3')
	return

def operateOff():
	arduinoData.write('0')
	return

def back():
	control_window.destroy()
	arduinoData.write('0')
	arduinoData.close()
	os.system("python device_controller.py")

def exitall():
	arduinoData.write('0')
	arduinoData.close()
	control_window.destroy()

control_window=Tk()

lab0=Label(text="To operate device 3")
lab1=Label(text="do click on respective choise")
lab2=Label(text="				")
lab3=Label(text="				")
lab4=Label(text="				")
lab5=Label(text="				")

btn1=Button(control_window,text='Switch ON',command=operateOn)
btn2=Button(control_window,text='Switch OFF',command=operateOff)
btn3=Button(control_window,text='Back',command=back)
btn4=Button(control_window,text='EXIT',command=exitall)

lab0.pack()
lab1.pack()
lab2.pack()
btn1.pack()
lab3.pack()
btn2.pack()
lab4.pack()
btn3.pack()
lab5.pack()
btn4.pack()

arduinoData = serial.Serial('com5',9600)

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
control_window.title("Operate Device 3")
control_window.mainloop()
