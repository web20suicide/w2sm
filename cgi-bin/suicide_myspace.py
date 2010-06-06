import random,time
import csv, logging, urllib
import re, sys, os
import settings,MySQLdb
#*******************************************************
# global settings
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)
#*******************************************************


def getInfo(sel,lastwords,command,email,password):
	sel.open("http://home.myspace.com/index.cfm?fuseaction=user")
	random_wait = random.randint(3,6)
	time.sleep(random_wait)
	capturepath = "/var/www/profiles/img/"
	filename = str(int(time.time())) + ".png"
	capture = capturepath + filename

	# get profile name and friends amount with regex-vodoo
	websource = sel.get_html_source()
	try:
		m = re.search('<a href="http://profile.myspace.com\/index.cfm\?fuseaction=user.viewprofile\&amp;friendID=(.*?)"',websource,re.IGNORECASE)
		friend_id = m.group(1)
		logging.info("friend ID is: " + friend_id)
	except:
		logging.warning("friend ID failed") 
		pass
	try:
		m = re.search('<div class="moduleBody">\n<a href=".*"><img alt="" src="(.*)"></a>',websource,re.IGNORECASE)
		profile_picture = m.group(1)
		logging.info("[ok] got the profile picture from " + username)
	except:
		logging.warning("[failed] profile picture regex failed!!!")
		#logging.error(websource)
		pass	
	try:
		logging.info("[ok] url of profile picture is " + profile_picture)
		urllib.urlretrieve(profile_picture, capture)
		logging.info("[ok] image moved to " + capture)
	except:
		logging.warning("[failed] profile picture download failed!!!")
		pass
	try:
		cropme = "convert %s -resize '200' %s" %(capture,capture)
		os.system(cropme)
		print cropme
		logging.info("[ok] image cropped to 200px width")
	except:
		logging.error("[failed] image not cropped")
		pass
	try:
		m = re.search('<span class="greeting">Hello,\s(.*)!</span>',websource,re.IGNORECASE)
		username = m.group(1)
		logging.info("[ok] username logged in as " + username)
		logging.info("[ok] " + username + " last words are " + lastwords)
	except:
		logging.warning("[failed] username regex failed!!!")
		logging.warning(websource)
		pass
	try:
		#logging.info("websource is: " + websource)
		m = re.search('<h3 class="moduleHead"><span><span>Friend\sSpace\s\((.*)\)</span></span></h3>',websource,re.IGNORECASE)
		friends = m.group(1)
		logging.info("[ok] " + username + " has " + friends + " friends!")
	except:
		logging.warning("[failed] friendsamount regex failed!!!")
		pass
	# sql query
	try:
		q = "INSERT INTO web20suicide.users(`id`,`username`,`friends`,`picture`,`lastwords`,`command`,`t_create`,`email`,`password`) VALUES (NULL,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,%s,%s)"
		cursor.execute(q, (username,friends,filename,lastwords,command,email,password,))
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
	return friends,user_id,friend_id

def changeLanguage(sel):
	sel.open("http://uk.myspace.com/")
	random_wait = random.randint(6,10)
	time.sleep(random_wait)
	websource = sel.get_html_source()
	time.sleep(1)
	try:
		m = re.search('<div class="popup_buttons"><input value="(.*?)" type="button"',websource,re.IGNORECASE)
		button_continue = "//input[@value='" + m.group(1) + "']"
		logging.info(button_continue)
		sel.click(button_continue)
		logging.info("[ok] language changed")
		random_wait = random.randint(4,6)
		time.sleep(random_wait)
		sel.refresh()
		random_wait = random.randint(4,6)
		time.sleep(random_wait)
	except:
		logging.info(websource)
		logging.error("[failed] changing language failed")
def delMyspace(sel,friend_id,friends):
	random_wait = random.randint(3,8)
	time.sleep(random_wait)
	website_friends = "http://friends.myspace.com/index.cfm?fuseaction=user.viewfriends&friendID=%s" %friend_id
	print website_friends
	sel.open(website_friends)
	random_wait = random.randint(3,6)
	time.sleep(random_wait)
	sel.click("//a[@id='ctl00_ctl00_ctl00_cpMain_cpMain_cpfMainBody_FriendsActions_EditModeLink']/b")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	looprunner = int(friends) / 40
	looprunner += 1
	logging.info("delete friend loop has to run " + str(looprunner) + " times")
	#try:
	i = 1
	if (friends == "0"):
		logging.info("user has no friends")
	else:
		for i in range(int(looprunner)):
			sel.click("selectAll")
			logging.info("selecting all works " + str(i))
			random_wait = random.randint(10,15)
			time.sleep(random_wait)
			try:
				sel.click("//button[@value='Delete Selected Friends']")
				random_wait = random.randint(8,15)
				time.sleep(random_wait)
				try:
					sel.get_confirmation()
					logging.info("clicked yes in alert dialog, catched the confirmation")
				except:
					sel.click("//button[@value='Delete Selected Friends']")
					random_wait = random.randint(8,15)
					sel.get_confirmation()
					pass
				random_wait = random.randint(10,15)
				time.sleep(random_wait)
				logging.info("huge delay")
				#sel.refresh()
				random_wait = random.randint(3,5)
				time.sleep(random_wait)
				logging.info("page refreshed")
				killed = i * 40
				logging.info("[ok] about " + str(killed+1) + "friends killed")
			except:
				logging.warning("something wrong with friend removal")
				try:
					sel.click("selectAll")
					random_wait = random.randint(1,2)
					time.sleep(random_wait)
					sel.click("selectAll")
					random_wait = random.randint(10,15)
					time.sleep(random_wait)
					sel.click("//button[@value='Delete Selected Friends']")
					random_wait = random.randint(8,15)
					time.sleep(random_wait)
					try:
						sel.get_confirmation()
						logging.info("clicked yes in alert dialog, catched the confirmation")
					except:
						sel.click("//button[@value='Delete Selected Friends']")
						random_wait = random.randint(8,15)
						sel.get_confirmation()
						pass
				except:
					logging.error("[failed] friend removal failed!!")
				pass
		#except:
		#	logging.warning("[failed] friends couldnt' be killed outside")
	return sel
def changeStatus(sel,message):
	sel.open("http://home.myspace.com/index.cfm?fuseaction=user")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	# sel.click("lnkUpdate")
	# random_wait = random.randint(5,8)
	# time.sleep(random_wait)
	# sel.click("ctl00_ctl00_cpMain_cpMain_UserStatus_statusInput")
	# random_wait = random.randint(1,4)
	# time.sleep(random_wait)
	sel.type("status", message) 
	random_wait = random.randint(2,4)
	time.sleep(random_wait)
	sel.click("//form[@id='statusMoodEditor']/div[3]/span/button")
	#sel.type("ctl00_ctl00_cpMain_cpMain_UserStatus_statusInput", message)
	#random_wait = random.randint(4,8)
	#time.sleep(random_wait)
	#sel.click("btnUpdate")
	random_wait = random.randint(5,10)
	time.sleep(random_wait)
	logging.info("[ok] status message changed!")

def logout(sel):
	random_wait = random.randint(3,8)
	time.sleep(random_wait)
	sel.open("http://signups.myspace.com/index.cfm?fuseaction=signup")
	logging.info("[ok] logging out now!")
	return sel

def changePicture(sel):
	sel.open("http://home.myspace.com/index.cfm?fuseaction=user")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	sel.click("ctl00_ctl00_cpMain_cpMain_Welcome_UploadChangePhotosHyperLink")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	sel.click("link=Upload Photos")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	sel.click("link=here")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	sel.click("//tr[@id='ctl00_ctl00_cpMain_cpMain_UserUploadPhotoControl_Upload1_trBasicUploaderLink']/td[2]/a")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	sel.type("ctl00_cpMain_ImageToUpload", "/usr/lib/cgi-bin/facebook_kill.jpg")
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.click("ctl00_cpMain_rdNewAlbum")
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.type("ctl00_cpMain_txtNewAlbumName", "suicidemachine")
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	sel.click("ctl00_cpMain_ButtonUpload")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
