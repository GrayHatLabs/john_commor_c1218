#How To:
#create PTS port on socat

socat -d -d pty,raw,echo=1 pty,raw,echo=1

#edit john_commor_c1218.py set serial to /dev/pts/x 

#where x is one of the new pts ports
#start termineter2

set connection /dev/pts/y 

#where /dev/pts/y is the other pts port number 

#start john_commer_cs1218.py
python john_commer_cs1218.py


