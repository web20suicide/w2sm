#!/usr/bin/python
import cgi,os,sys,urllib
import subprocess
import settings, MySQLdb
import json

# connect db (settings.py)
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)

print "Content-type: text/html"
print 

def checkAvailable ():
	run = subprocess.Popen('ps ax | grep \"Xtightvnc :[0-9]\" | awk \'{printf $6\" \"}\' | sed s/://g', shell=True, stdout=subprocess.PIPE).communicate()[0][:-1].split()

	# this is implemented to help preventing racing problems and the latency we have in launching VNC
	q = "SELECT claimed FROM sessions WHERE NOW()-last_reserved < 5"
	cursor.execute(q)
	listclaimed = []
	# get all the "claimed" or reserved ports and make a list
	while (1):
		ports = cursor.fetchone()
		if ports == None:
			break
		listclaimed.append(ports['claimed'])
	# append the reservation list to the running VNC sessions list
	for i in listclaimed:
		run.append(str(i))
	claimed = []
	if '1' in run or '2' in run:
		claimed.append("facebook")
	if '3' in run or '4' in run:
		claimed.append("myspace")
	if '5' in run or '6' in run:
		claimed.append("twitter")
	if '7' in run or '8' in run:
		claimed.append("linkedin")

	returnstring = ""
	for i in claimed:
		returnstring += i
		returnstring += "<|>"
	print returnstring 
	return claimed

checkAvailable()
