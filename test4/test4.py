import serial
import time
from Tkinter import *

def led_on1():
	arduinoData.write('1')
	return

def led_on2():
	arduinoData.write('2')
	return

def led_on3():
	arduinoData.write('3')
	return

def led_on4():
	arduinoData.write('4')
	return

def led_off():
	arduinoData.write('0')
	return

led_control_window=Tk()

lab0=Label(text="A GUI Application for controling LED Bulbs using python buttons")
lab1=Label(text="To switch ON the first LED")
lab2=Label(text="To switch ON the second LED")
lab3=Label(text="To switch ON the third LED")
lab4=Label(text="To switch ON the fourth LED")
lab5=Label(text="To switch OFF the LED(s)")


btn1=Button(led_control_window,text='led 1 ON',command=led_on1)
btn2=Button(led_control_window,text='led 2 ON',command=led_on2)
btn3=Button(led_control_window,text='led 3 ON',command=led_on3)
btn4=Button(led_control_window,text='led 4 ON',command=led_on4)
btn5=Button(led_control_window,text='led OFF',command=led_off)

lab0.pack()

lab1.pack()
btn1.pack()

lab2.pack()
btn2.pack()

lab3.pack()
btn3.pack()

lab4.pack()
btn4.pack()

lab5.pack()
btn5.pack()

arduinoData = serial.Serial('com5',9600)

led_control_window.mainloop()
