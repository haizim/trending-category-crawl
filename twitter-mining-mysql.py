from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from time import sleep 
import time
import datetime
import csv

import mysql.connector

mydb = mysql.connector.connect(
  host=[host],
  user=[user],
  password=[pass],
  database=[db_name]
)

print "---------------------------------------------"
chrome_options = Options()
#chrome_options.add_argument("--user-data-dir=/home/haizim/py/selenium/user-data/")
#chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--headless")
#options = webdriver.ChromeOptions()

driver = webdriver.Chrome("/home/haizim/chrome-driver/chromedriver",options=chrome_options)
driver.set_window_position(-10000,10000,windowHandle='current')
driver.get("https://twitter.com/i/trends")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 580);")
print "580"
driver.execute_script("window.scrollTo(0, 980);")
print "980"
time.sleep(5)

print "*********************************************"
n=0
rows, cols = (20, 4)
trend = [[0 for i in range(cols)] for j in range(rows)]
#print trend
for k in driver.find_elements_by_class_name('r-j7yic'):
	#print "*********************************************"
	#print n
	trend[n][0] = n #n
	trend[n][1] = "" #trend
	trend[n][2] = "" #category
	trend[n][3] = "" #trending with

	
	for t in k.find_elements_by_class_name('r-vmopo1'):
		trend[n][1] = t.text
		#print "trend :",tr
	for c in k.find_elements_by_class_name('r-1wbh5a2'):
		kat = c.text
		if(kat.find("Trending with") != -1):
			kat = kat.replace("Trending with ","")
			trend[n][3] = kat
			#print "Trending with ",dgn
		else:
			trend[n][2] = kat
			#print "category : ",cat
	#print trend[n][0]
	#print trend
	if(trend[n][2] != "Trends"):
		print trend[n][0],". ",trend[n][1]," // ",trend[n][2]," // ",trend[n][3]
		n +=1

driver.quit()
#trend[n+1][0]=25
#print trend

print "*********************************************"

for x in trend:
	if(x[1]!=0):
		
		cek = "select * from key_indo where trend='"+x[1]+"'"
		#print "cek : ",cek
		cursor = mydb.cursor()
		cursor.execute(cek)
		res = cursor.fetchone()

		if(cursor.rowcount<1):
			masuk = "insert into key_indo(trend,kategori,terbaru) values ('"+x[1]+"','"+x[2]+"','"+x[2]+"')"
			ntf = "baru >> "+x[1]+" : "+x[2]
		else:
			if x[2] not in res[3]:
				katbar = res[3]+" "+x[2]
				masuk = "update key_indo set kategori='"+katbar+"', terbaru='"+x[2]+"' where trend='"+x[1]+"'"
				ntf = "tambah >> "+x[1]+" : "+katbar
			else:
				masuk = "update key_indo set terbaru='"+x[2]+"' where trend='"+x[1]+"'"
				ntf = "udah ada >> "+x[1]
		
		cursorr = mydb.cursor()
		cursorr.execute(masuk)
		print ntf