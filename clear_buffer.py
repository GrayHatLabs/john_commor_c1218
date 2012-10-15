import serial

ser = serial.Serial('/dev/pts/1')
ser2 = serial.Serial('/dev/pts/2')


while 1: 
	print repr(ser.read(1))
	print repr(ser2.read(1))
