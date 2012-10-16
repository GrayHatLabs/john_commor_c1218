import serial	

ser = serial.Serial('/dev/pts/1')
ser.flushInput()
ser.flushOutput()

ser2 = serial.Serial('/dev/pts/2')
ser2.flushInput()
ser2.flushOutput()
ser2.close()

connect1 = '\xee\x00\x00\x00\x00\x01\x20\x13\x10'
connect2 = '\x06\xee\x00\x20\x00\x00\x05\x61\x01\x00\x01\x06\x81\xd2'
connect3 = '\x06\xee\x00\x00\x00\x00\x0d\x50\x00\x00\x30\x30\x30\x30\x20\x20\x20\x20\x20\x20\x76\x35'
connect4 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x00\x5f\x7f'
connect5 = '\x06\xee\x00\x00\x00\x00\x01\x21\x9a\x01'
ACK = '\x06'
R = '\xee'
NACK = '\x15'

frame = ''
connect1_success = 0
connect2_success = 0
connect3_success = 0
connect4_success = 0
connect5_success = 0

while 1:
	line = ser.read(1)
	frame += line
	if connect2_success == 1:
		print 'line = ' + repr(line) 
		print 'frame = ' + repr(frame) 

	if frame == connect1:
		ser.write(ACK)
		ser.write('\xee\x00\x20\x00\x00\x05')
		payload = '\x00\x00\x01\x00\x00'
		chksum = '\xff\x42'
		ser.write(payload)
		ser.write(chksum)
		frame = ''
		print 'cleared frame = ' + frame 
		connect1_success = 1

	elif frame == connect2 and connect1_success == 1:
		ser.write(ACK)
		ser.write('\xee\x00\x00\x00\x00\x05')
		payload = '\x00\x01\x00\x01\x06'
		chksum = '\x4f\x8f'
		ser.write(payload)
		ser.write(chksum)
		frame = ''
		print 'cleared frame 2 =' + repr(frame)
		connect2_success = 1

	elif frame == connect3 and connect2_success == 1:
		ser.write(ACK)
		ser.write('\xee\x00\x20\x00\x00\x01')
		payload = '\x00'
		chksum = '\x80\x51'
		ser.write(payload)
		ser.write(chksum)
		frame = ''
		print 'cleared frame 3 =' + repr(frame)
		connect3_success = 1

	elif frame == connect4 and connect3_success == 1:
		ser.write(ACK)
		ser.write('\xee\x00\x00\x00\x00\x62')
		payload = '\x00\x00\x5e\x02\x0a\x8a\x47\x45\x20\x20\x02\x00\x08\x0c\x02\x00\x0f\x0f\x03\x0c\x01\x04\xef\xf9\xe1\x9e\x03\x00\x78\xe0\x81\x19\x00\x00\x00\x80\x0b\x01\x00\x00\x00\x00\x00\x00\x00\x7c\x5c\x30\x60\x00\x86\xff\x79\x06\x23\x0f\x00\x00\x00\x00\x00\x00\x00\xdf\xda\x71\x08\xe0\xf8\xe1\x02\x03\x00\x68\x60\x80\x08\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x5c\x14\x10\x60\x00\x82\x84\x9e'
		chksum = '\x4c\x75'
		ser.write(payload)
		ser.write(chksum)
		frame = ''
		print 'cleared frame 4 =' + repr(frame)
		connect4_success = 1
	
	elif frame == connect5 and connect4_success == 1:
		ser.write(ACK)
		ser.write('\xee\x00\x20\x00\x00\x01')
		payload = '\x00'
		chksum = '\x80\x51'
		ser.write(payload)
		ser.write(chksum)
		print 'cleared frame 4 = ' + repr(frame)
		connect5_success = 1 


	
