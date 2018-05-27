import serial
import time
from Tkinter import *

def led_on():
	arduinoData.write('1')

def led_off():
	arduinoData.write('0')

led_control_window=Tk()
btn1=Button(led_control_window,text='led ON',command=led_on)
btn2=Button(led_control_window,text='led OFF',command=led_off)

btn1.pack()
btn2.pack()

arduinoData = serial.Serial('com5',9600)

led_control_window.mainloop()
