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
	ftp = FTP(server)
	ftp.login(username, password)
	f = open("arduino.txt", 'w+')
	a = s.receive()
	d = a[1]
	if 'degF' in d:
		t = d['degF']
		f.write(str(t))
		f1 = open("arduino.txt", "rb")
		ftp.storbinary("STOR weather.txt", f1)
		f1.close()
	else:
		pass
	f.close()
	ftp.quit()
	time.sleep(1)
