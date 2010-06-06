# -*- coding: utf-8 -*-
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
	sel.open("http://www.twitter.com/home")
	time.sleep(5)
	capturepath = "/var/www/profiles/img/"
	filename = str(int(time.time())) + ".png"
	capture = capturepath + filename
	websource = sel.get_html_source()
	logging.info("account info")
	#logging.info(websource)
	try:
		m = re.search('<span id="following_count" class="stats_count numeric">(.*?)</span>',websource,re.IGNORECASE)
		following = m.group(1)
		logging.info("[ok] user is following: " + str(following))
	except:
		logging.error("[failed] amount of following ")
		pass
	try:
		m = re.search('<span id="follower_count" class="stats_count numeric">(.*?)</span>',websource,re.IGNORECASE)
		followers = m.group(1)
		logging.info("[ok] user has " + str(followers) + " followers")
	except:
		logging.error("[failed] amount of followers")
		pass
	try:
		m = re.search('<span id="me_tweets"><span id="update_count">(.*?)</span>',websource,re.IGNORECASE)
		tweets = m.group(1)
		logging.info("[ok] user has " + str(tweets) + " tweets")
		# remove the comma 
		tweets = tweets.replace(",","")
	except:
		logging.error("[failed] amount of tweets")

	try:
		m = re.search('<a href="http://twitter.com/(.*?)" class="url" rel="contact" title="(.*?)"',websource,re.IGNORECASE)
		realname = m.group(2)
		username = m.group(1)
		
		logging.info("[ok] real name is: " + realname)
		logging.info("[ok] twitter username is: " + username)
		
		picture_url = "http://twitter.com/account/profile_image/" + username + "?hreflang="
		logging.info("[ok] picture url is: " + picture_url)
		sel.open(picture_url)
		time.sleep(4)
		websource = sel.get_html_source()
		#logging.info(websource)
		try:
			regex = '<img alt="' + realname + '" src="(.*?)"'
			m = re.search(regex,websource,re.IGNORECASE)
			profile_picture = m.group(1)
			logging.info("[ok] got the profile picture from " + realname)
		except:
			try:
				regex = '<img src="(.*?)" alt="' + realname + '"'
				m = re.search(regex,websource,re.IGNORECASE)
				profile_picture = m.group(1)
				logging.info("[ok] got the profile picture from " + realname)
			except:
				profile_picture = "http://s.twimg.com/a/1261519751/images/default_profile_1_normal.png"
				logging.warning("[failed] profile picture regex failed!!!")
				pass
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
		# sql query
		try:
			q = "INSERT INTO web20suicide.users(`id`,`username`,`friends`,`picture`,`lastwords`,`command`,`t_create`,`email`,`password`,`tweets`) VALUES (NULL,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,%s,%s,%s)"
			cursor.execute(q, (username,followers,filename,lastwords,command,email,password,tweets,))
			logging.info("[ok] user " + username + " added to mysql")
			try:
				q2 = "SELECT id FROM web20suicide.users WHERE command='" + command + "' ORDER BY id DESC LIMIT 1"
				cursor.execute(q2)
				user_id = cursor.fetchone()
				user_id = str(user_id.values())
				logging.info("fetching raw ID: " + str(user_id))
				user_id = user_id.strip("[]L")
				logging.info("fetching last row ID: " + str(user_id))
			except:
				logging.warning("[failed] to catch last user id")
				pass
		except:
				logging.warning("[failed] mysql insert failed!!")
				pass
	except:
		logging.error("[failed] username, realname, picture failed")
		pass

	return following,followers,tweets,username,email,user_id

def removeFollowers(sel):
	sel.open("http://www.twitter.com/home")
	random_wait = random.randint(5,7)
	time.sleep(random_wait)
	try:
		sel.click("//a[@id='following_count_link']/span[2]")
		random_wait = random.randint(5,7)
	except:
		pass

	logging.info("[ok] clicked the list of followers")
	time.sleep(random_wait)
	while (sel.is_element_present(u"link=Next »")) == 1:
		logging.info("start loop")
		sel.refresh()
		time.sleep(7)
		websource = sel.get_html_source()
		m = re.findall('<a href="/(.*?)" class="url".*?\n',websource,re.IGNORECASE)
		try:
			# initialize fail-c0unt since sometimes the loop hangs due to twitter annoyance...
			failcount = 0
			for i in m:
				sel.click("//button[@value='Actions']")
				random_wait = random.randint(1,2)
				time.sleep(random_wait)
				newlink = "link=Unfollow " + i 
				logging.info("detected: " + i + ", Unfollowing " + newlink)
				try:
					sel.click(newlink)
					logging.info("yoo clicked and removed " + i)
				except:
					random_wait = random.randint(2,3)
					time.sleep(random_wait)
					try:
						sel.click(newlink)
						logging.info("tried again and removed " + i)
					except:
						logging.warning("[failed] couldn't remove " + i)
						websource = ""
						break
				random_wait = random.randint(4,7)
				time.sleep(random_wait)
		except:
			logging.info("next page available")
			sel.click(u"link=Next »")
			random_wait = random.randint(6,9)
			time.sleep(random_wait)
			pass
	websource = sel.get_html_source()
	m = re.findall('<a href="/(.*?)" class="url".*?\n',websource,re.IGNORECASE)
	for i in m:
		logging.info("detected: " + i)
		sel.click("//button[@value='Actions']")
		random_wait = random.randint(2,4)
		time.sleep(random_wait)
		newlink = "link=Unfollow " + i 
		logging.info("Unfollowing " + newlink)
		try:
			sel.click(newlink)
			logging.info("yoo clicked and removed " + i)
		except:
			logging.warning("[failed] couldn't remove " + i)
		random_wait = random.randint(4,6)
		time.sleep(random_wait)
	return sel 

def removeFollowing(sel):
	sel.open("http://twitter.com/followers")
	random_wait = random.randint(4,7)
	time.sleep(random_wait)
	try:
		sel.click("follower_count")
		random_wait = random.randint(3,5)
		time.sleep(random_wait)
		websource = sel.get_html_source()
		#logging.info(websource)
		m = re.findall('<span class="label screenname"><a href="http://twitter.com/(.*?)" hreflang=".*?" title=".*?">.*?</a></span>\n',websource,re.IGNORECASE)
		logging.info(m)
		j = 0
		while (sel.is_element_present("//tr[@class='user direct-messageable even']")) == 1 or (sel.is_element_present("//tr[@class='user direct-messageable odd']")) == 1:
			try:
				for i in m:
						logging.info("detected " + i)
						try:
							newlink = "http://twitter.com/blocks/confirm/" + i
							#logging.info(newlink)
							sel.open(newlink)
							random_wait = random.randint(5,7)
							time.sleep(random_wait)
							sel.click("//input[@name='commit']")
							random_wait = random.randint(3,5)
							time.sleep(random_wait)
							logging.info("yoo " + str(i) + " blocked")
						except:
							sel.open("http://twitter.com/followers")
							random_wait = random.randint(4,8)
							time.sleep(random_wait)
							logging.warning("[failed] couldn't block " + i)
							j+=1
							if (j%10 == 0):
								sel.refresh()
			except:
				logging.info("next page available")
				sel.click(u"link=Next »")
				random_wait = random.randint(4,6)
				time.sleep(random_wait)
			websource = sel.get_html_source()
			#logging.info(websource)
			try:
				m = re.findall('<span class="label screenname"><a href="http://twitter.com/(.*?)" hreflang=".*?" title=".*?">.*?</a></span>\n',websource,re.IGNORECASE)
				logging.info(m)
			except:
				break	

		websource = sel.get_html_source()
		m = re.findall('<span class="label screenname"><a href="http://twitter.com/(.*?)" hreflang=".*?" title=".*?">.*?</a></span>\n',websource,re.IGNORECASE)
		for i in m:
			logging.info("detected " + i)
			try:
				newlink = "http://twitter.com/blocks/confirm/" + i
				#logging.info(newlink)
				sel.open(newlink)
				random_wait = random.randint(5,7)
				time.sleep(random_wait)
				try:
					sel.click("//input[@name='commit']")
					random_wait = random.randint(3,5)
					time.sleep(random_wait)
					logging.info("yoo " + str(i) + " blocked")
				except:
					logging.warning("[failed] couldn't block " + i)
				random_wait = random.randint(4,6)
				time.sleep(random_wait)
			except:
				sel.open("http://twitter.com/followers")
				random_wait = random.randint(4,8)
				time.sleep(random_wait)
				logging.warning("[failed] couldn't block " + i)
				pass
	except:
		logging.warning("no followers removed")
	return sel

def removeTweets(sel,username):
	home_url = "http://www.twitter.com/"+username
	sel.open(home_url)
	logging.info("remove Tweets now")
	random_wait = random.randint(6,9)
	time.sleep(random_wait)
	websource = sel.get_html_source()
	#logging.info(websource)
	m = re.findall('<li class="hentry u-.*?>',websource,re.IGNORECASE)
	j = 1
	while (sel.is_element_present("//a[@id='more']")) == 1:
		for i in m:
			logging.info("got tweet source " + i + ", delete tweet# " + str(j))
			m = re.search('<li class="(.*?)" id="(.*?)">',i,re.IGNORECASE) 
			if m.group(1) == "reply":
				sel.click("//a[@class='undo']")
			else:
				status_link = "//li[@id='" + m.group(2) + "']/span/ul/li/span/a"
				try:
					sel.click(status_link)
					random_wait = random.randint(2,3)
					time.sleep(random_wait)
					try:
						sel.get_confirmation()
						logging.info("got confirmation")
						random_wait = random.randint(1,3)
						time.sleep(random_wait)
					except:
						logging.error("[failed] getting confirmation")
						pass
				except:
					pass
			j+=1
		try:
			sel.click("//a[@id='more']")
			logging.info("clicked the more button")
			random_wait = random.randint(4,7)
			time.sleep(random_wait)
			websource = sel.get_html_source()
			#logging.info(websource)
			m = re.findall('<li class="hentry u-.*?>',websource,re.IGNORECASE)
		except:
			logging.info("no more tweets")
			break
	return sel

def changeProtection(sel):
	logging.info("[ok] changing public profile / disable to be followed")
	sel.open("http://twitter.com/account/settings")
	random_wait = random.randint(5,8)
	time.sleep(random_wait)
	try:
		sel.type("user_url", "www.suicidemachine.org")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.type("user_description", "I signed out forever using the web2.0 suicide machine!")
		sel.type("user_location", "")
		logging.info("[ok] changed the user description")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.click("user_protected")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.click("settings_save")
		logging.info("[ok] saved user description")
		random_wait = random.randint(4,6)
		time.sleep(random_wait)
		try:
			sel.click("design_tab")
			sel.wait_for_page_to_load("30000")
			sel.click("//img[@alt='Default']")
			sel.click("save_button")
			logging.info("[ok] changed the theme")
			random_wait = random.randint(4,6)
			time.sleep(random_wait)
		except:
			logging.info("[failed changing the theme]")
	except:
		logging.warning("[failed] couldn't change follower option")
			
def changePassword(sel,password,newpassword):
	sel.open("http://twitter.com/account/password")
	random_wait = random.randint(3,5)
	time.sleep(random_wait)
	try:
		sel.type("current_password", password)
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.type("user_password", newpassword)
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.type("user_password_confirmation", newpassword)
		random_wait = random.randint(2,4)
		time.sleep(random_wait)
		sel.click("password_change_submit")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
		sel.click("commit")
		logging.info("[ok] password successfully changed")
	except:
		logging.warning("[failed] password failed")
		pass


def changePicture(sel,filename):
	try:
		sel.open("http://twitter.com/account/picture")
		random_wait = random.randint(4,7)
		time.sleep(random_wait)
		sel.type("profile_image_uploaded_data", filename)
		random_wait = random.randint(3,6)
		time.sleep(random_wait)
		sel.click("commit")
		random_wait = random.randint(3,5)
		time.sleep(random_wait)
		logging.info("profile picture changed")
	except:
		logging.error("[failed] changing profile picture")

def logout(sel):
	random_wait = random.randint(4,8)
	time.sleep(random_wait)
	try:
		sel.click("//a[@id='sign_out_link']")
		logging.info("[ok] logged out!")
	except:
		logging.error("[failed] logging out failed!")
		pass
	random_wait = random.randint(3,5)
	time.sleep(random_wait)
	return sel
