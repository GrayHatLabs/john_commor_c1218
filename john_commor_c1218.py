import serial
import binascii
import sys
import getopt


class power_meter():

	ACK = '\x06'
	R = '\xee'
	NACK = '\x15'

	def __init__(self,pts_term,pts_com):

		#add input check here
		self.PTS_TERM = pts_term
		self.PTS_COM = pts_com
		self.ACK = '\x06'
		self.R = '\xee'
		self.NACK = '\x15'
		#self.ser_term = serial.Serial('/dev/pts/'+self.PTS_TERM)
		try:
			self.ser_com = serial.Serial('/dev/pts/' + self.PTS_COM)
		except:
			print 'Error could not open '+ '/dev/pts/' + self.PTS_COM 
			print "\nMaybe wrong PTS?"
			print "\n"
			sys.exit()

		self.flush_pts_term()
		self.flush_pts_com()


	def flush_pts_term(self):

		try:
			ser2 = serial.Serial('/dev/pts/' + self.PTS_TERM)
			ser2.flushInput()
			ser2.flushOutput()
			ser2.close()
		except:
			print "Error: Could not flush /dev/pts/" + self.PTS_TERM
			print "\nMaybe wrong PTS?"
			sys.exit()
			

	def flush_pts_com(self):
		self.ser_com.flushInput()
		self.ser_com.flushOutput()


	def check(self,frame):
		
		print binascii.hexlify(frame)

		if self.connect_check(frame):
			print 'connect_check found : ' + binascii.hexlify(frame)
			return True

		if self.read_table(frame):
			print 'read_table_0 found: ' + binascii.hexlify(frame)
			return True

		if self.read_table1(frame):
			print 'read_table_1found: ' + binascii.hexlify(frame)
			return True

		if self.read_table2(frame):
			print 'read_table_2 found: ' + binascii.hexlify(frame)
			return True

		if self.read_table3(frame):
			print 'read_table_3 found: ' + binascii.hexlify(frame)
			return True

		if self.read_table4(frame):
			print 'read_table_4 found: ' + binascii.hexlify(frame)
			return True

		if self.read_table5(frame):
			print 'read_table_5 found: ' + binascii.hexlify(frame)
			return True

		if self.read_table6(frame):
			print 'read_table_6 found: ' + binascii.hexlify(frame)
			return True
			

		

		
	def read_table(self,frame):

		read_table0_0 = '\x06\xee\x00\x20\x00\x00\x01\x20\x82\x70'	
		read_table0_1 = '\x06\xee\x00\x00\x00\x00\x05\x61\x01\x00\x01\x06\xb8\x25'
		read_table0_2 = '\x06\xee\x00\x20\x00\x00\x0d\x50\x00\x00\x30\x30\x30\x30\x20\x20\x20\x20\x20\x20\xb4\x24'
		read_table0_3 =	'\x06\xee\x00\x00\x00\x00\x15\x51\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x10\xc8'
		read_table0_4 = '\x06\xee\x00\x20\x00\x00\x01\x21\x0b\x61'

		read_table_again0_0 = '\x06\xee\x00\x00\x00\x00\x01\x20\x13\x10'
		read_table_again0_1 = '\x06\xee\x00\x20\x00\x00\x05\x61\x01\x00\x01\x06\x81\xd2'
		read_table_again0_2 = '\x06\xee\x00\x00\x00\x00\x0d\x50\x00\x00\x30\x30\x30\x30\x20\x20\x20\x20\x20\x20\x76\x35'
		read_table_again0_3 = '\x06\xee\x00\x20\x00\x00\x15\x51\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x70\x47'
		read_table_again0_4 = '\x06\xee\x00\x00\x00\x00\x01\x21\x9a\x01'

		#read_table0_5 = '\x06\xee\x00\x20\x00\x00\x15\x51\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x70\x47'
		#ee0020000001208270
		if frame == read_table0_0 or read_table_again0_0 == frame:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x05')
			payload = '\x00\x00\x01\x00\x00'
			chksum = '\xff\x42'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		#ee00000000056101000106b825
		elif frame == read_table0_1 or read_table_again0_1 == frame:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x00\x00\x00\x05')
			payload = '\x00\x01\x00\x01\x06'
			chksum = '\x4f\x8f'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True
		
		#ee002000000d50000030303030202020202020b424
		elif frame == read_table0_2 or read_table_again0_2 == frame:
			self.ser_com.write(self.ACK)
			#\xee\x00\x20\x00\x00\x01
			self.ser_com.write('\xee\x00\x20\x00\x00\x01')
			payload = '\x00'
			chksum = '\x80\x51'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		#ee000000001551000000000000000000002020202020202020202010c8
		elif frame == read_table0_3 or read_table_again0_3 == frame:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x00\x00\x00\x01')
			payload = '\x01'
			chksum = '\x98\x20'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		#ee0020000001210b61
		elif frame == read_table0_4 or read_table_again0_4 == frame:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x01')
			payload = '\x00'
			chksum = '\x80\x51'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		return False



	def read_table1(self,frame):

		#read_table1_2 =	'\x06\xee\x00\x00\x00\x00\x15\x51\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x10\xc8'
		read_table1_3 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x01\xd6\x6e'
		read_table1_4 = '\x06\xee\x00\x00\x00\x00\x01\x21\x9a\x01'
		
		read_table = 'ee0000000003300002ce3f'	
		#if frame == read_table1_2:
		#	self.ser_com.write(self.ACK)
		#	self.ser_com.write('\xee\x00\x20\x00\x00\x01')
		#	payload = '\x00'
		#	chksum = '\x80\x51'
		#	self.ser_com.write(payload)
		#	self.ser_com.write(chksum)
		#	return True

		if frame == read_table1_3:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x24')
			payload = '\x00\x00\x20\x47\x45\x20\x20\x49\x32\x31\x30\x2b\x63\x20\x20\x01\x09\x02\x00\x33\x38\x30\x31\x38\x30\x32\x32\x20\x20\x20\x20\x20\x20\x20\x20\xe6'
			chksum = '\xca\x09'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		elif frame == read_table1_4:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x00\x00\x00\x01')
			payload = '\x00'
			chksum = '\x11\x31'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		return False

	def read_table2(self,frame):
		
		read_table2 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x02\x4d\x5c'		
		
		if frame == read_table2:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\x06\xee\x00\x20\x00\x00\x25')
			payload = '\x00\x00\x21\x31\x2e\x30\x00\x00\x00\x31\x2e\x30\x00\x00\x00\x01\x20\x20\x20\x20\x32\x4b\x00\x05\x32\x30\x30\x00\x00\x00\x33\x30\x00\x00\x00\x00\xea'
			chksum = '\x63\x5c'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		return False
	
	def read_table3(self,frame):

		read_table3 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x03\xc4\x4d'

		if frame == read_table3:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x09')
			payload = '\x00\x00\x05\x01\x40\x00\x00\x00\xbf'
			chksum = '\x74\xb4'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		return False

	def read_table4(self,frame):

		#read_table4 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x04\x7b\x39'
		read_table4 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x04\x7b\x39'
		if frame == read_table4:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x01')
			payload = '\x05'
			chksum = '\x2d\x06'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True


		return False
	
	def read_table5(self,frame):
		read_table5 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x05\xf2\x28'

		if frame == read_table5:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x18')
			payload = '\x00\x00\x14\x20\x20\x30\x33\x38\x30\x31\x38\x30\x32\x32\x20\x20\x20\x20\x20\x20\x20\x20\x20\xd8'
			chksum = '\xc7\x71'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		return False

	def read_table6(self,frame):
		read_table6 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x06\x69\x1a'

		if frame == read_table6:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\xea')
			payload = binascii.a2b_hex('0000e6000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000030202020202020202020302020202020202020203020202020202020202000000000000000000000000000000000000000003031323334353637383900000000000000000000000000000000000000000000000000000000000003')
			chksum = '\x47\x29'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		return False





	def connect_check(self,frame):
		#print repr(frame)
		connect1 = '\xee\x00\x00\x00\x00\x01\x20\x13\x10'
		connect2 = '\x06\xee\x00\x20\x00\x00\x05\x61\x01\x00\x01\x06\x81\xd2'
		connect3 = '\x06\xee\x00\x00\x00\x00\x0d\x50\x00\x00\x30\x30\x30\x30\x20\x20\x20\x20\x20\x20\x76\x35'
		connect4 = '\x06\xee\x00\x20\x00\x00\x03\x30\x00\x00\x5f\x7f'
		connect5 = '\x06\xee\x00\x00\x00\x00\x01\x21\x9a\x01'

		if frame == connect1:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x05')
			payload = '\x00\x00\x01\x00\x00'
			chksum = '\xff\x42'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		elif frame == connect2:

			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x00\x00\x00\x05')
			payload = '\x00\x01\x00\x01\x06'
			chksum = '\x4f\x8f'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		elif frame == connect3:

			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x01')
			payload = '\x00'
			chksum = '\x80\x51'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True

		elif frame == connect4:

			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x00\x00\x00\x62')
			payload = '\x00\x00\x5e\x02\x0a\x8a\x47\x45\x20\x20\x02\x00\x08\x0c\x02\x00\x0f\x0f\x03\x0c\x01\x04\xef\xf9\xe1\x9e\x03\x00\x78\xe0\x81\x19\x00\x00\x00\x80\x0b\x01\x00\x00\x00\x00\x00\x00\x00\x7c\x5c\x30\x60\x00\x86\xff\x79\x06\x23\x0f\x00\x00\x00\x00\x00\x00\x00\xdf\xda\x71\x08\xe0\xf8\xe1\x02\x03\x00\x68\x60\x80\x08\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x5c\x14\x10\x60\x00\x82\x84\x9e'
			chksum = '\x4c\x75'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			return True
	
		elif frame == connect5:
			self.ser_com.write(self.ACK)
			self.ser_com.write('\xee\x00\x20\x00\x00\x01')
			payload = '\x00'
			chksum = '\x80\x51'
			self.ser_com.write(payload)
			self.ser_com.write(chksum)
			#self.flush_pts_com()

			return True
		return False

def usage():
	print "Please enter both pts ports for \n termineter2 and the power meter emulator."
	print "\n Example python john_commers.py -t 1 -e 2"


def main():

	pts_1 = None
	pts_2 = None
	#catch options
	try:
		opts, args = getopt.getopt(sys.argv[1:], "t:e:")
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)
	for o, a in opts:
		if o == "-t":
			pts_1 = a
		elif o == "-e":
			pts_2 = a
		
	if(pts_1 == None or pts_2 == None):
		usage()
		sys.exit(2)
	
	pm = power_meter(pts_1,pts_2) 
	frame = ''
	print "Power Meter Emulator Started \n"
	print "Use /dev/pts/"+ pts_1 +" to connect to in termineter2 "

	while 1:

		line = pm.ser_com.read(1) 
		frame += line
		if pm.check(frame):
			print 'found' 
			frame = ''

		# if the frame has two \xee then we have two write operation in the frame and we need to clear
		#if frame.count('\xee') > 1 :
			#print 'reset found'
			#frame = '\x06\xee'
	

if __name__ == '__main__' :
	main()
