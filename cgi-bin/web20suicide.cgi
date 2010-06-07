#!/usr/bin/python
from selenium import selenium
from pyfiglet import Figlet
import settings,MySQLdb
import suicide_twitter
import suicide_facebook
import suicide_myspace
import unittest, time, re
import os, sys, select
import random,cgi
import csv
import subprocess
import logging
from logging import handlers, Formatter

# GLOBAL USER SETTINGS -- CHANGE THIS!!!!!
newpassword = "chuckn0rr1s"

#*******************************************************
# global settings
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)
#*******************************************************

f = Figlet(font='slant',zipfile='/home/killer/pyfiglet-0.4/fonts.zip') # or zipfile=PATH

def figlet_counter(f):
	print f.renderText("3")
	time.sleep(0.8)
	print f.renderText("2")
	time.sleep(0.8)
	print f.renderText("1")
	time.sleep(0.8)

def kill_all():
	killpython = "killall -9 python"
	killjava = "killall -9 java"
	os.system(killjava)
	os.system(killpython)

def send_notification(name,user_id):
	SENDMAIL = "/usr/sbin/sendmail" # sendmail location
	logging.info("opening sendmail")
	p = os.popen("%s -t" % SENDMAIL, "w")
	receiver = "TO: " + name + "\n"
	sender = "FROM: suicide@moddr.net\n" 
	p.write(sender)
	p.write(receiver)
	p.write("Subject: Your 2.0 memorial page\n")
	p.write("")
	p.write("Dear 2.0 Suicider,\n\nYour personal memorial page is available here: http://www.suicidemachine.org/memorial.php?id=" + user_id) # blank line separating headers from body
	p.write("\n\nPlease accept our deepest sympathy for your decision. We all know that there's a better life out there!\n\nPlease do not hesitate to help your friends and relatives commit suicide today, forward them the link http://suicidemachine.org!\n\nSincerly,\nYour 2.0 Suicide Team")
	sts = p.close()
	if sts != 0:
		print "Sendmail exit status", sts
		logging.info("mail sent to " + name)

def send_error_mail(name):
	SENDMAIL = "/usr/sbin/sendmail" # sendmail location
	logging.info("opening sendmail")
	p = os.popen("%s -t" % SENDMAIL, "w")
	receiver = "TO: " + name + "\n" 
	sender = "FROM: suicide@moddr.net\n" 
	p.write(sender)
	p.write(receiver)
	p.write("Subject: Your 2.0 suicide attempt encountered complications\n")
	p.write("Hello,\n\nUnfortunately, our machine ran into troubles while executing a rather complicated 2.0 suicide on your profile.\nThis can happen due to new API restrictions, server lag or simple your wish to resurrect yourself.\nPlease visit www.suicidemachine.org again to give your suicide attempt another chance!\n\nIn case you feel utterly dissappointed, please send us an email to suicide@moddr.net and someone will immediately take care of your removal.\n\nSincerly,\nYour 2.0 Suicide Team") 
	# blank line separating headers from body
	sts = p.close()
	if sts != 0:
		print "Sendmail exit status", sts
		logging.info("mail sent to " + name)

def send_login_error(name):
	SENDMAIL = "/usr/sbin/sendmail" # sendmail location
	logging.info("opening sendmail")
	p = os.popen("%s -t" % SENDMAIL, "w")
	receiver = "TO: " + name + "\n" 
	sender = "FROM: suicide@moddr.net\n" 
	p.write(sender)
	p.write(receiver)
	p.write("Subject: Your 2.0 suicide attempt went wrong\n")
	p.write("Hello,\n\nUnfortunately you provided a wrong password. Please try logging in again with your correct login details.\n\nPlease visit www.suicidemachine.org to give your suicide attempt another chance!\n\nSincerly,\nYour 2.0 Suicide Team") 
	# blank line separating headers from body
	sts = p.close()
	if sts != 0:
		print "Sendmail exit status", sts
		logging.info("mail sent to " + name)

def quit_log(vnc):
	logging.debug("session ending at "+time.asctime())
	log_filename = "/tmp/suicide_log.out%s" %vnc
	logging.debug(log_filename)
	logging.info("**********************************************************************************")
	cmd = "tail -n 40 %s" %log_filename
	log_content = os.popen(cmd).read()
	log_content += "vnc server: %s" %vnc 
	SENDMAIL = "/usr/sbin/sendmail" # sendmail location
	p = os.popen("%s -t" % SENDMAIL, "w")
	p.write("To: killer@yugo.at\n")
	p.write("Subject: suicide machine\n")
	p.write(log_content) # blank line separating headers from body
	sts = p.close()
	if sts != 0:
			print "Sendmail exit status", sts
	
# selenium functions
def login_process(name, password,website,port,vnc,f,lastwords,session_id):
	try:
		#sel = selenium("localhost", port, "*firefoxproxy", website)
		# firefoxproxy doesn't work if selenium-rc is called with forcedBrowserMOde
		#sel = selenium("localhost", port, "*firefoxproxy", website)
		sel = selenium("localhost", port, "*chrome", website)
		sel.start()
		if (website == "http://www.facebook.com"):
			website = "https://login.facebook.com/login.php"
		sel.open_window(website,"koobecaf")
		sel.select_window("koobecaf")
		sel.set_timeout(120000)
	except:
		logging.error("selenium login failed")
		quit_log(vnc)
	time.sleep(5)
	figlet_counter(f)
	cmd2 = "for i in `ls -d /tmp/custom*`; do cp /home/killer/.mozilla/firefox/ze0ym9mm.77777/cert8.db /home/killer/.mozilla/firefox/ze0ym9mm.77777/cert_override.txt $i;done"
	override_db = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
	sel.window_maximize()
	# go fullscreen by simulating F11 button press
	sel.key_press("//","\\122")
	#sel.refresh()
	#################################################
	# facebook - hate your friends
	################################################
	if website == "https://login.facebook.com/login.php":
		sel.type("//input[@id='email']", name)
		time.sleep(1)
		sel.mouse_down("//input[@id='email']")
		sel.mouse_up("//input[@id='email']")
		time.sleep(1)
		sel.key_press("//","9")
		sel.key_press("//input[@id='email']","\9")
		sel.key_press("//input[@id='email']","\\9")
		sel.type("pass",password)
		time.sleep(1)
		sel.click("//input[@value='Login']")
		random_wait = random.randint(7,14)
		time.sleep(random_wait)
		try:
			sel.open("http://www.facebook.com/editaccount.php?ref=mb")
			random_wait = random.randint(1,4)
			time.sleep(random_wait)
			sel.open("https://register.facebook.com/editaccount.php?language")
			random_wait = random.randint(1,4)
			time.sleep(random_wait)
			sel.select("locale", "label=English (US)")
			random_wait = random.randint(5,10)
			time.sleep(random_wait)
			logging.info("[ok] language changed")
			sel.click("link=Profile")
			random_wait = random.randint(7,14)
			time.sleep(random_wait)
			logging.info("[ok] logged in now")
		except:
			logging.error("[failed] logged failed")
			tearDown(sel)
			logging.warning("login failed")
			logging.warning("sending login warning to: " + name)
#send_login_error(name)
#			quit_log(vnc)
			os.system("python /usr/lib/cgi-bin/web20clean_database.cgi 2> /dev/null")
			print f.renderText("wrong password! please try again!")
			print f.renderText("your activity has been logged!")
			random_wait = random.randint(2,4)
			time.sleep(random_wait)
			print f.renderText("aborting suicide now..!")
			figlet_counter(f)
			kill_all()
	#################################################
	# twitter 
	################################################
	elif website == "http://www.twitter.com":
		random_wait = random.randint(1,4)
		time.sleep(random_wait)
		sel.click("topnav")
		random_wait = random.randint(1,4)
		time.sleep(random_wait)
		sel.click("//div[@id='topnav']/a/span")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.type("username", name)
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.type("password", password)
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.click("signin_submit")
		random_wait = random.randint(6,10)
		time.sleep(random_wait)
		if (sel.is_element_present("status")) != 1:
			logging.warning("[failed] form id=statusMoodEditor is now present. shutting down!")
			quit_log(vnc)
			tearDown(sel)
			os.system("python /usr/lib/cgi-bin/web20clean_database.cgi 2> /dev/null")
			print f.renderText("wrong password!")
			print f.renderText("your activity has been logged!")
			random_wait = random.randint(5,12)
			time.sleep(random_wait)
			print f.renderText("aborting suicide now..!")
			time.sleep(1)
			figlet_counter(f)
			time.sleep(1)
#kill_vnc(vnc,session_id)
		logging.info("[ok] logged in now")

	#################################################
	# myspace 
	################################################
	elif website == "http://www.myspace.com":
		try:
			random_wait = random.randint(1,3)
			time.sleep(random_wait)
			sel.type("ctl00_ctl00_cpMain_cpMain_LoginBox_Email_Textbox", name)
			sel.type("ctl00_ctl00_cpMain_cpMain_LoginBox_Password_Textbox", password)
			random_wait = random.randint(1,3)
			time.sleep(random_wait)
			# click logging button
			sel.click("dlb")
			logging.info("[ok] trying to login now!")
			random_wait = random.randint(6,12)
			time.sleep(random_wait)
			try:
				# confirm language question with submit
				sel.click("Submit")
				time.sleep(5)
			except:
				pass
			if (sel.is_element_present("statusMoodEditor")) != 1:
				logging.warning("[failed] form id=statusMoodEditor is now present. shutting down!")
				print "login failed"
				quit_log(vnc)
				tearDown(sel)
				os.system("python /usr/lib/cgi-bin/web20clean_database.cgi 2> /dev/null")
				print f.renderText("wrong password!")
				print f.renderText("your activity has been logged!")
				random_wait = random.randint(5,12)
				time.sleep(random_wait)
				print f.renderText("aborting suicide now..!")
				time.sleep(1)
				figlet_counter(f)
				time.sleep(1)
#kill_vnc(vnc,session_id)
			logging.info("[ok] logged in now")
		except:
			tearDown(sel)
			send_login_error(name)
			quit_log(vnc)
			os.system("python /usr/lib/cgi-bin/web20clean_database.cgi 2> /dev/null")
			print f.renderText("wrong password!")
			print f.renderText("your activity has been logged!")
			random_wait = random.randint(5,12)
			time.sleep(random_wait)
			print f.renderText("aborting suicide now..!")
			random_wait = random.randint(1,3)
			time.sleep(random_wait)
			figlet_counter(f)
			time.sleep(1)
#kill_vnc(vnc,session_id)

def tearDown(sel):
	sel.stop()
	return sel

########################################
# THIS IS THE MAIN LOOP 
###################################################
while 1:
	job_id = sys.argv[1]
 	# select recent post
	q = "SELECT * FROM friendbot WHERE job_id = '"+job_id+"' ORDER BY t_create"
	cursor.execute(q)
	# get current row
	row = cursor.fetchone()
	time.sleep(1.5)

	if (row != None):
		command = row['command']
		variables = row['data'] # get the data out of da base
		variables = cgi.parse_qs(variables) # parse urlstring into dictionary
		raw_variables = row['data'] # keep some raw for latter url calls
		password = variables.get('password')[0]
		website = variables.get('website')[0]
		name = variables.get('username')[0]
		port = variables.get('port')[0]
		vnc = variables.get('vnc')[0]
		ip = variables.get('ip')[0]
		host = variables.get('host')[0]
		lastwords = variables.get('lastwords')[0]
		session_id = variables.get('session_id')[0]

		# delete fetched row, clean the commando database
		q = "DELETE FROM friendbot WHERE id=%s"
		cursor.execute(q, (row['id'],))

		try:
			log_filename = "/tmp/suicide_log.out%s" %vnc
			logging.basicConfig(filename=log_filename,level=logging.DEBUG,)
			logging.info("**********************************************************************************")
			logging.info("new session starting: "+time.asctime())
			logging.info("session ID used for firefox is: " + session_id)
			logging.info("userIP: " + ip + " @ " + host)
			logging.info("website: "+ website)
			logging.info("user: " + name + " using password: "+password)

			print "*** commando received..trying to login with account %s now on %s using port %s ***" %(name,website,port)
			print "*** in 15seconds you will be given a virtual lethal injection ... ***"
			print f.renderText("suicide machine is booting ...")
			print f.renderText("stay calm ...")
			print ""
			passwordtxt = "password is *******"
			print f.renderText(passwordtxt)

			######################################################
			# FACEBOOK
			#######################################################
			if(row['command'] == "facebook"):
				print "*** getting rid of your friends... ***"
				time.sleep(4) # don't hurry
				suicide_facebook.changePassword(sel,password,newpassword)
				logging.info("[ok] changed password")
				amount,user_id = suicide_facebook.getInfo(sel,lastwords,command,name,password)
				suicide_facebook.unNotify(sel)
				#suicide_facebook.removeInfo(sel)
				suicide_facebook.changePicture(sel,"/usr/lib/cgi-bin/killer.jpg"," went to Web2.0 Suicide Machine and left this empty frontpage... Visit http://suicide.moddr.net to find out more!")
				logging.info("[ok] changed picture")
				time.sleep(4) # don't hurry
				# GS added: stupid facebook change made this function deprecated 14.09.09
				#suicide_facebook.changeStatus(sel," went to Web2.0 Suicide Machine and left this empty frontpage... Visit http://suicide.moddr.net to find out more!")
				logging.info("[ok] changed status")
				suicide_facebook.removeFriends(sel,amount)
				logging.info("[ok] removed friends")
				suicide_facebook.delPosts(sel)
				suicide_facebook.delGroups(sel)
				suicide_facebook.removeFriends(sel,amount)
				suicide_facebook.joinGroup(sel)
				time.sleep(4) # don't hurry
				logging.info("[ok] joined the Social Network Suicider Group")
				suicide_facebook.logout(sel)
				logging.info("[ok] tear down selenium. killing done")
				tearDown(sel) # close selenium
				print f.renderText("killing done ... quitting now")
				print ""
				random_wait = random.randint(5,12)
				time.sleep(random_wait)

			######################################################
			# MYSPACE 
			#######################################################
			elif(row['command'] == "myspace"):
				print "*** yo, get rid of your myspaceness... ***"
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				suicide_myspace.changeLanguage(sel)
				friends,user_id,friend_id = suicide_myspace.getInfo(sel,lastwords,command,name,password)
				suicide_myspace.delMyspace(sel,friend_id,friends)
				suicide_myspace.changeStatus(sel," went to the Web 2.0 Suicide Machine and left this lousy frontpage... Visit http://www.suicidemachine.org for more info!!!")
				suicide_myspace.logout(sel)
				tearDown(sel) # close selenium
				quit_log(vnc)
				print f.renderText("killing done ... quitting now")
				print ""
				random_wait = random.randint(3,5)
				time.sleep(random_wait)
			######################################################
			# TWITTER 
			#######################################################
			elif(row['command'] == "twitter"):
				print "*** yo, get rid of your tweets... ***"
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				logging.info("[ok] logged in nwo")
				suicide_twitter.changePassword(sel,password,newpassword)
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				following,followers,tweets,username,name,user_id = suicide_twitter.getInfo(sel,lastwords,command,name,password)
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				suicide_twitter.changePicture(sel,"/usr/lib/cgi-bin/killer.jpg")
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				suicide_twitter.changeProtection(sel)
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				suicide_twitter.removeFollowers(sel)
				suicide_twitter.removeFollowing(sel)
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				suicide_twitter.removeTweets(sel,username)
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				suicide_twitter.removeFollowers(sel)
				suicide_twitter.removeFollowing(sel)
				suicide_twitter.removeTweets(sel,username)
				suicide_twitter.logout(sel)
				tearDown(sel) # close selenium
				quit_log(vnc)
				print f.renderText("killing done ... quitting now")
				print ""
				random_wait = random.randint(3,5)
				time.sleep(random_wait)
		
			send_notification(name,user_id)	
			quit_log(vnc)
#kill_vnc(vnc,session_id)
		######################################################
		# EXCEPTION HANDLER 
		#######################################################
		except:
			logging.exception("[failed] There was a problem. Please report!")
			logging.info("Ending SUICIDE MACHINE")
			send_error_mail(name)
			quit_log(vnc)
#kill_vnc(vnc,session_id)
