import scratch
import time
from ftplib import FTP
print 'Welcome to the S4A Weather Station project.'
print 'Please open S4A now.'
server = str(raw_input('Please type in your FTP server\'s address. '))
username = str(raw_input('FTP username? (leave blank for anonymous) '))
password = str(raw_input('FTP password? '))
s = scratch.Scratch()
s.connect()

while(True):
	a = s.receive()
	d = a[1]
	if 'degF' in d:
		ftp = FTP(server)
		ftp.login(username, password)
		t = d['degF']
		f = open("arduino.txt", "w")
		f.write(str(t))
		f.close()
		f1 = open("arduino.txt", "rb")
		ftp.storbinary("STOR arduino.txt", f1)
		f1.close()
		ftp.quit()
		print t
	time.sleep(5)
