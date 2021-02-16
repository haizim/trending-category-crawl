import time
import os
import datetime
from datetime import datetime



#while True:
while True:
	now = datetime.now()

	current_time = now.strftime("%A %d,%B,%Y %H:%M:%S")
	print("****************************************************")
	print("Current Time =", current_time)
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
	os.system('python twitter-mining-mysql.py')
	sekarang = datetime.now()
	current = sekarang.strftime("%H:%M:%S")
	print "Sudah >> ", current
	time.sleep(600)
