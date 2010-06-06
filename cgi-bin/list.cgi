#!/usr/bin/python
import cgi,os,sys,urllib
import subprocess
import settings, MySQLdb

# connect db (settings.py)
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)

print "Content-type: text/html"
print 

# get environ variables
requested_url= os.environ

form = cgi.FieldStorage() 

command = form.getvalue('id')
name = form.getvalue('username')

def ReturnVncPort (command,name):
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
	####################################################
	####################################################
	#				 _  ____________.---------.    
	#					\`'  __________|_________|  
	#					/   (_)__]                  
	#				 |    |                       
	#				.'   .'                         
	#				|____]                    
	#
	#####################################################
	# SET DEBUG TO 1 TO DISABLE USER SESSIONS
	####################################################
	debug = "0"
	#####################################################
	####################################################
	####################################################
	####################################################
	####################################################
	####################################################
	if debug == "1":
		port = "none"
		if command == 'facebook' and name == 'indowist@gmx.at':
			port = '1'
		elif command == 'facebook' and name == 'sven.markmann@newpic.de':
			port = '1'
		elif command == 'facebook' and name == 'gordo@yugo.at':
			port = '6'
		elif command == 'facebook' and name == 'online@wormweb.nl':
			port = '1'
		elif command == 'facebook' and name == 'gordo@wormweb.nl':
			port = '8'
		elif command == 'facebook' and name == 'milfbar@gmail.com':
			port = '2'
		elif command == 'twitter' and name == 'gordo@yugo.at':
			port = '1'
	else:
		if command == 'facebook' and '1' not in run:
			port = '1'
		elif command == 'facebook' and '2' not in run:
			port = 'none'
		elif command == 'facebook':
			port = 'none'
		elif command == 'myspace' and '3' not in run:
			port = '3'
		elif command == 'myspace' and '4' not in run:
			port = 'none'
		elif command == 'myspace':
			port = 'none'
		elif command == 'twitter' and '5' not in run:
			port = '5'
		elif command == 'twitter' and '6' not in run:
			port = 'none'
		elif command == 'twitter':
			port = 'none'
		elif command == 'linkedin' and '7' not in run:
			port = '7'
		elif command == 'linkedin':
			port = 'none'

	# if there's a port given to new user make a reservation by updating timestamp
	if port != 'none':
		q2 = "UPDATE sessions SET last_reserved=NOW() WHERE claimed = " + port + " LIMIT 1"
		cursor.execute(q2)

	print port
	return port

ReturnVncPort(command,name)

