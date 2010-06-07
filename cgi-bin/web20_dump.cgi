#!/usr/bin/python
import cgi,os,sys,urllib
import settings, MySQLdb
import random,time
import subprocess

# connect db (settings.py)
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)

print "Content-type: text/html"
print 

print """<html><head>

</head>"""
# get environ variables
requested_url= os.environ


form = cgi.FieldStorage() 

command = form.getvalue('command')
username = form.getvalue('username')
password = form.getvalue('password')
website = form.getvalue('website')
job_id = form.getvalue('id')
ip = form.getvalue('ip') 
host = form.getvalue('host')


# create random number for SESSION ID
session_id = int(random.random()*1000000000)

try:
	lastwords = form.getvalue('lastwords')
except:
	lastwords = "no comment"
	pass

# create vnc and selenium ports ranging from 4440-4449 and associated VNC ports 5900-5909
data = "command=" + str(command) + "&username=" + str(username) + "&password=" + str(password) + "&website=" + str(website) + "&port=444" + str(job_id) + "&vnc=" + str(job_id) + "&ip=" + str(ip) + "&host=" + str(host) + "&lastwords=" + str(lastwords) + "&session_id=" + str(session_id)

job_id = str(job_id)
# dump data for temporary database
q = "INSERT INTO web20suicide.friendbot(`id`,`command`,`data`,`job_id`,`t_create`) VALUES (NULL,%s,%s,%s,CURRENT_TIMESTAMP)"

# commit SQL :P
cursor.execute(q, (command,data,job_id,))

# start selenium server on port 444x (1-9) 
seleniumport = "444" + job_id
cmd4 = """sudo -u killer -H sh -c 'DISPLAY=:0 xterm -geometry 170x24+0+463 -e "sh /usr/lib/cgi-bin/start_selenium.sh %s 2> /var/www/tmp/error_selenium%s.log"&'"""%(seleniumport,job_id)
launch_selenium= subprocess.Popen(cmd4, shell=True, stdout=subprocess.PIPE)


# start python suicide script (sys.argv=job_id 1-9) in xterm (sudo -u killer -H sh -c is needed because xauth needs to be explictily started by killer user!)
cmd3 = """DISPLAY=:0 xterm -geometry 170x36+0+0 -e "python /usr/lib/cgi-bin/web20suicide.cgi %s 2> /var/www/tmp/error_python%s.log" &""" %(job_id,job_id)
launch_python = subprocess.Popen(cmd3, shell=True, stdout=subprocess.PIPE)


print "</html>"
