import serial	

ser = serial.Serial('/dev/pts/7')

while 1:
	print repr(ser.read())
	
