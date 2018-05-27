# step 1
#pip install Pyserial
import serial

# step 2
ser=serial.Serial('COM3',9600)

# step 3
while 1:
	val=raw_input("enter 0 or 1 to control LED : ");
	ser.write(val)