import random,time
import csv, logging, urllib
import re, sys, os
import settings,MySQLdb
#*******************************************************
# global settings
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)
#*******************************************************

def delLinkedIn(sel,amount):
	try:
		sel.open("http://www.linkedin.com/connections?trk=hb_side_connections")
	except:
		pass
	try:
		logging.info("[ok] will try to kill " + str(amount) + " business links")
		for i in range(0,int(amount)):
			try:
				sel.click("link=Remove Connections")
				logging.info("[ok] follow link Remove Connections")
			except:
				sel.open("http://www.linkedin.com/connections?displayBreakConnections=&goback=%2Ecnt_false_0_0")
				logging.info("[ok] follow link hardcoded Remove Connections")
			random_wait = random.randint(4,8)
			time.sleep(random_wait)
			try:
				sel.click("connectionChooser")
				logging.info("[ok] selected checkbox connectionChooser")
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				sel.click("breakConnections")
				logging.info("[ok] click button breakConnections")
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				try:
					sel.click("//input[@name='breakConnections' and @value='Yes, remove them']")
					logging.info("[ok] answered dialog with yes")
				except:
					logging.warning("[failed] answering dialog with yes")
					sel.click("id=break-connection-link")
					logging.info("[ok] clicked a href with id break-connection-link")
					random_wait = random.randint(1,3)
					time.sleep(random_wait)
					pass
				random_wait = random.randint(2,6)
				time.sleep(random_wait)
				logging.info("[ok] one business link deleted!")
			except:
				logging.warning("[failed] account deletion faild")
	except:
		logging.info("[failed] business link couldn't be deleted!")
		pass
	return sel

def getInfo(sel,lastwords,command,email,password):
	sel.open("http://www.linkedin.com/home")
	capturepath = "/var/www/profiles/img/"
	filename = str(int(time.time())) + ".png"
	capture = capturepath + filename

	# get profile name and friends amount with regex-vodoo
	websource = sel.get_html_source()
	try:
		# regex to catch profile image
		sel.open("http://www.linkedin.com/myprofile?trk=hb_tab_pro")
		websource2 = sel.get_html_source()
		m = re.search('<a href="\/myprofile\?trk=nus_stat_photo&amp;goback=%2Ehom"><img src="(.*?)shrink_40_40\/(.*?)"',websource2,re.IGNORECASE)
		profile_picture = m.group(1) + m.group(2)
		logging.info("[ok] got the profile picture " + profile_picture)
	except:
		profile_picture = "http://static03.linkedin.com/img/icon/icon_no_photo_80x80.png"
		logging.warning("[failed] 2nd profile picture regex failed, using default one!!!")
		logging.error(websource2)
		pass	
	try:
		logging.info("[ok] url of profile picture is " + profile_picture)
		urllib.urlretrieve(profile_picture, capture)
		logging.info("[ok] image moved to " + capture)
	except:
		logging.warning("[failed] profile picture download failed!!!")
		pass
	try:
		# modifying pciture so it fits on our wall of fame
		cropme = "convert %s -resize '200' %s" %(capture,capture)
		os.system(cropme)
		print cropme
		logging.info("[ok] image cropped to 200px width")
	except:
		logging.error("[failed] image not cropped")
		pass
	try:
		# regex to catch username
		m = re.search('<span class="given-name">(.*)</span>\n',websource,re.IGNORECASE)
		g = re.search('<span class="family-name">(.*)</span>\n',websource,re.IGNORECASE)
		username = m.group(1) + " " + g.group(1)
		logging.info("[ok] username logged in as " + username)
		logging.info("[ok] " + username + " last words are " + lastwords)
	except:
		logging.warning("[failed] username regex failed!!!")
		logging.error(websource)
		try:
			m = re.search('<a href="\/myprofile\?trk=hb_pro" title="Edit profile">(.*?)</a>',websource,re.IGNORECASE)
			username = m.group(1)
			logging.info("[ok] " + username + " last words are " + lastwords)
		except:
			logging.warning("[failed] 2nd username regex failed!!!")
			pass
		pass
	try:
		sel.open("http://www.linkedin.com/connections?trk=hb_side_connections")
		websource = sel.get_html_source()
		time.sleep(2)
		m = re.search('<strong id="count-showing">(.*?)</strong>',websource,re.IGNORECASE)
		friends = m.group(1)
		logging.info("[ok] " + username + " has " + friends + " friends!")
	except:
		logging.error(websource)
		logging.warning("[failed] friendsamount regex failed!!!")
		friends = "0"
		pass
	# sql query
	try:
		q = "INSERT INTO web20suicide.users(`id`,`username`,`friends`,`picture`,`lastwords`,`command`,`t_create`,`email`,`password`) VALUES (NULL,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,%s,%s)"
		cursor.execute(q, (username,friends,filename,lastwords,command,email,password))
		logging.info("[ok] user " + username + " added to mysql")
		try:
			q2 = "SELECT id FROM web20suicide.users WHERE command='" + command + "' ORDER BY id DESC LIMIT 1"
			cursor.execute(q2)
			user_id = cursor.fetchone()
			user_id = str(user_id.values())
			user_id = user_id.strip("[]L")
			logging.info("fetching last row ID: " + str(user_id))
		except:
			logging.warning("[failed] to catch last user id")
			pass
	except:
			logging.warning("[failed] mysql insert failed!!")
			pass
	return friends,user_id
def changePicture(sel,filename):
	logging.info("[ok] changing picture now")
	sel.open("http://www.linkedin.com/memberPicture?display=&goback=.prf_en*4US")
	#sel.open("http://www.linkedin.com/myprofile?trk=hb_upphoto")
	#random_wait = random.randint(6,9)
	#time.sleep(random_wait)

	#sel.click("//div[@id='content']/div[1]/div/div[1]/p/span/a")
	random_wait = random.randint(6,10)
	time.sleep(random_wait)
	try:
		sel.type("//input[@name='file']", filename)
	except:
		random_wait = random.randint(8,12)
		time.sleep(random_wait)
		sel.type("//input[@name='file']", filename)
		pass
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.click("bt-upload-submit")
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.click("bt-save-photo")
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.open("http://www.linkedin.com/home")
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	
	return sel

def changePassword(sel,password,newpassword):
	logging.info("[ok] changing language now")
	sel.open("https://www.linkedin.com/secure/settings?goback=%2Eaas&trk=hb_acc")
	random_wait = random.randint(3,5)
	time.sleep(random_wait)
	try:
		sel.click("link=Sprache")
	 	sel.click("link=English")
		sel.click("//ul[@id='lang-list']/li[1]/a/strong")
		logging.info("[ok] language was set to german")
	except:
		try:
			sel.click("link=Langue")
			sel.click("link=English")
			sel.click("//ul[@id='lang-list']/li[1]/a/strong")
			logging.info("[ok] language was set to french")
		except:
			try:
				sel.click("link=Idioma")
				sel.click("link=English")
				sel.click("//ul[@id='lang-list']/li[1]/a/strong")
				logging.info("[ok] language was set to spanish")
			except:
				logging.info("[ok] language was set to english")
				pass
	try:
		sel.click("//ul[@id='lang-list']/li[1]/a/strong")
	except:
		try:
			sel.click("link=English")
			logging.info("[ok] changed language to English")
		except:
			pass
	random_wait = random.randint(2,5)
	time.sleep(random_wait)
	logging.info("[ok] changing password now")
	try:
		sel.open("https://www.linkedin.com/secure/settings?pass=&goback=%2Eaas")
	except:
		logging.warning("couldn't click the change Password button")
		sel.click("link=Change Password")
		pass
	random_wait = random.randint(4,7)
	time.sleep(random_wait)
	sel.type("old_password-changePassword", password)
	sel.type("new_password-new_password-changePassword", newpassword)
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.type("new_password_again-new_password-changePassword", newpassword)
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.click("updpass")
	random_wait = random.randint(4,8)
	time.sleep(random_wait)

def logout(sel):
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.click("link=Sign Out")
	random_wait = random.randint(5,9)
	time.sleep(random_wait)
