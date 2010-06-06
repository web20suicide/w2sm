import random,time
import csv, logging, urllib
import re, sys, os
import settings,MySQLdb
#*******************************************************
# global settings
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)
#*******************************************************

def changeStatus(sel,status_message):
	try:
		sel.open("http://www.facebook.com/home.php?ref=home")
		random_wait = random.randint(5,8)
		time.sleep(random_wait)
	except: 
		pass
	sel.type("//div[@class='Mentions_Input']",status_message)
	random_wait = random.randint(4,8)
	time.sleep(random_wait)
	time.sleep(1)
	sel.click("//input[@value='Share']")
	random_wait = random.randint(7,10)
	time.sleep(random_wait)

def logout(sel):
	random_wait = random.randint(6,12)
	time.sleep(random_wait)
	try:
		sel.click("link=Logout")
	except:
		sel.click("//div[@id='fb_menu_logout']/div/a/span")
		pass
	logging.info("[ok] logged out!")
	random_wait = random.randint(6,12)
	time.sleep(random_wait)

def unNotify(sel):
	logging.info("[ok] unnotifing the whole shebang!")
	sel.open("http://www.facebook.com/editaccount.php?notifications")
	time.sleep(3)
	sel.uncheck("notif_setting_email_msg")
	sel.uncheck("notif_setting_email_friend")
	sel.uncheck("notif_setting_email_friend_confirmed")
	sel.uncheck("notif_setting_email_wall")
	sel.uncheck("notif_setting_email_poke")
	time.sleep(1)
	sel.uncheck("notif_setting_email_birthday_reminder")
	sel.uncheck("notif_setting_email_friend_detail_req")
	sel.uncheck("notif_setting_email_family_request")
	sel.uncheck("notif_setting_email_family_confirm")
	sel.uncheck("notif_setting_email_friend_suggestion")
	sel.uncheck("notif_setting_email_friend_suggestion_accepted")
	sel.uncheck("notif_setting_email_invitee_joined")
	sel.uncheck("notif_setting_email_mention")
	sel.uncheck("notif_setting_email_mentions_comment")
	sel.uncheck("notif_setting_email_photo_tag")
	sel.uncheck("notif_setting_email_photo_tag_request")
	sel.uncheck("notif_setting_email_photo_comment")
	sel.uncheck("notif_setting_email_photo_comment_tagged")
	sel.uncheck("notif_setting_email_photo_reply")
	sel.uncheck("notif_setting_email_photo_upload_via_email")
	sel.uncheck("notif_setting_email_photo_album_comment")
	sel.uncheck("notif_setting_email_photo_album_reply")
	sel.uncheck("notif_setting_email_group_invite")
	sel.uncheck("notif_setting_email_group_add_officer")
	time.sleep(1)
	sel.uncheck("notif_setting_email_group_admin")
	sel.uncheck("notif_setting_email_group_r2j")
	sel.uncheck("notif_setting_email_board_post_reply")
	sel.uncheck("notif_setting_email_group_name_change")
	sel.uncheck("notif_setting_email_fbpage_admin")
	sel.uncheck("notif_setting_email_fbpage_fan_invite")
	sel.uncheck("notif_setting_email_event_invite")
	sel.uncheck("notif_setting_email_event_update")
	sel.uncheck("notif_setting_email_event_cancel")
	sel.uncheck("notif_setting_email_event_admin")
	sel.uncheck("notif_setting_email_event_r2j")
	sel.uncheck("notif_setting_email_event_wall")
	sel.uncheck("notif_setting_email_event_name_change")
	sel.uncheck("notif_setting_email_note_tag")
	sel.uncheck("notif_setting_email_note_comment")
	sel.uncheck("notif_setting_email_note_reply")
	sel.uncheck("notif_setting_email_share_comment")
	sel.uncheck("notif_setting_email_share_reply")
	sel.uncheck("notif_setting_email_video_tag")
	sel.uncheck("notif_setting_email_video_tag_request")
	sel.uncheck("notif_setting_email_video_comment")
	sel.uncheck("notif_setting_email_video_comment_tagged")
	sel.uncheck("notif_setting_email_video_reply")
	sel.uncheck("notif_setting_email_answers_answered")
	sel.uncheck("notif_setting_email_gift_received")
	sel.uncheck("notif_setting_email_answers_best_answer")
	sel.uncheck("notif_setting_email_feed_comment")
	sel.uncheck("notif_setting_email_feed_comment_reply")
	sel.uncheck("notif_setting_email_stale_email")
	sel.uncheck("notif_setting_email_product_news")
	sel.uncheck("notif_setting_email_research_invite")
	time.sleep(2)
	sel.click("save_notifications")
	logging.info("[ok] unchecked all email notifications")
	time.sleep(4)
	sel.open("http://www.facebook.com/settings/?tab=privacy&section=search#/settings/?tab=privacy&section=search")
	time.sleep(5)
	try:
		sel.click("close")
		time.sleep(2)
	except:
		pass
	try:
		sel.uncheck("search_filter_public")
		time.sleep(2)
		sel.click("confirm")
		time.sleep(2)
		logging.info("[ok] excluded person from public search")
	except:
		pass

def joinGroup(sel):
	random_wait = random.randint(2,4)
	time.sleep(random_wait)
	try:
		sel.type("q", "Social Network Suiciders")
		random_wait = random.randint(3,5)
		time.sleep(random_wait)
		try:
			sel.click("//div[@id='universal_search_submit']/a/span")
			random_wait = random.randint(2,4)
			time.sleep(random_wait)
			sel.click("link=SNS - Social Network Suiciders")
		except:
			sel.click("hidden_button")
			sel.click("//label[@id='label_hidden_button']/span")
			pass
		random_wait = random.randint(3,5)
		time.sleep(random_wait)
		try:
			sel.click("link=Join Group")
			random_wait = random.randint(3,5)
			time.sleep(random_wait)
			sel.click("join")
			random_wait = random.randint(2,4)
			time.sleep(random_wait)
		except:
			try:
				sel.click("link=SNS - Social Network Suiciders")
				random_wait = random.randint(3,5)
				time.sleep(random_wait)
				sel.click("join")
				random_wait = random.randint(2,4)
				time.sleep(random_wait)
			except:
				pass
		pass
	except:
		logging.warning("joining group failed in first place")

def removeInfo(sel):
	logging.info("removing all personal information")
	sel.click("link=Profile")
	random_wait = random.randint(5,9)
	time.sleep(random_wait)
	sel.click("//ul[@id='profile_tabs']/li[2]/a/div/div[2]")
	time.sleep(5)
	sel.click("info_edit_all")
	time.sleep(5)
	sel.uncheck("sex_visibility")
	sel.click("//select[@id='birthday_visibility']/option[3]")
	sel.type("hometown_geo_sq", "")
	sel.type("current_city_sq", "")
	sel.type("hometown_geo_neighborhood_str", "")
	sel.click("//select[@id='family_relation[0]']/option[1]")
	sel.type("family_name[0]", "")
	sel.uncheck("meeting_sex2")
	sel.uncheck("meeting_sex1")
	sel.uncheck("meeting_for1")
	sel.uncheck("meeting_for2")
	sel.uncheck("meeting_for3")
	sel.uncheck("meeting_for6")
	sel.type("political_party_sq", "")
	sel.type("religion_name", "")
	sel.click("info_section_save_basic")
	time.sleep(2)
	sel.click("//div[@id='info_section_header_personal']/h3")
	time.sleep(2)
	sel.type("clubs", "")
	sel.type("interests", "")
	sel.type("music", "")
	sel.type("tv", "")
	sel.type("movies", "")
	sel.type("books", "")
	sel.type("quote", "")
	sel.type("about_me", "")
	sel.click("info_section_save_personal")
	time.sleep(2)
	sel.type("new_sn_0", "")
	sel.type("mobile", "")
	sel.type("other_phone", "")
	sel.type("address", "")
	sel.click("current_geo_sq")
	sel.type("current_geo_sq", "")
	sel.type("current_geo_neighborhood_str", "")
	sel.type("zip", "")
	sel.type("website", "")
	sel.click("info_section_save_contact")
	time.sleep(3)
	sel.type("education_college_1_school_name", "")
	sel.type("education_college_1_concentration1_name", "")
	sel.type("education_hs_1_school_name", "")
	sel.type("work_history_1_company", "")
	sel.type("work_history_1_position", "")
	sel.type("work_history_1_description", "")
	sel.click("work_history_1_location_sq")
	sel.type("work_history_1_location_sq", "")
	sel.click("work_history_1_workspan_current")
	sel.click("info_section_save_eduwork")
	time.sleep(3)

def changePassword(sel,password,newpassword):
	random_wait = random.randint(1,2)
	time.sleep(random_wait)
	try:
		sel.click("//li[@id='fb_menu_settings']/div/a")
	except:
		try:
			sel.click("//div[@id='fb_menu_settings']/div/a/span")
		except:
			sel.open("http://www.facebook.com/editaccount.php?settings")
	random_wait = random.randint(5,10)
	time.sleep(random_wait)
	try:
		sel.click("password_link_change")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
	except:
		random_wait = random.randint(5,10)
		time.sleep(random_wait)
		sel.click("password_link_change")
		random_wait = random.randint(1,2)
		time.sleep(random_wait)
	sel.type("old_password", password)
	sel.type("new_password", newpassword)
	random_wait = random.randint(1,2)
	time.sleep(random_wait)
	sel.type("confirm_password", newpassword)
	sel.click("save_password")
	random_wait = random.randint(2,5)
	time.sleep(random_wait)

def changePicture(sel,filename,message):
	try:
		sel.open("/editprofile.php")
	except:
		random_wait = random.randint(3,7)
		time.sleep(random_wait)
		sel.open("/editprofile.php")
		
	random_wait = random.randint(4,7)
	time.sleep(random_wait)
	try:
		sel.type("pic",filename)
		random_wait = random.randint(3,6)
		time.sleep(random_wait)
	except:
		sel.type("pic",filename)
		random_wait = random.randint(3,7)
		time.sleep(random_wait)
	sel.click("agree")
	random_wait = random.randint(3,5)
	time.sleep(random_wait)
	try:
		sel.click("uploadbutton")
	except:
		time.sleep(2)
		sel.clickAndWait("uploadbutton",60000)
	random_wait = random.randint(3,8)
	time.sleep(random_wait)
	try:
		sel.type("feedform_user_message", message)
		random_wait = random.randint(2,5)
		time.sleep(random_wait)
		sel.click("publish")
	except:
		logging.info("[failed] updating status message!")
		pass
	random_wait = random.randint(3,6)
	time.sleep(random_wait)
	
	return sel

def delGroups(sel):
	logging.info("trying to remove all groups")
	sel.click("link=Profile")
	random_wait = random.randint(3,7)
	time.sleep(random_wait)
	i = 0
	# navigating to group pages
	try:
		sel.click("//ul[@id='profile_tabs']/li[2]/a/div/div[2]")
		random_wait = random.randint(4,7)
		time.sleep(random_wait)
	except:
		random_wait = random.randint(5,10)
		time.sleep(random_wait)
		sel.click("//ul[@id='profile_tabs']/li[2]/a/div/div[2]")
		random_wait = random.randint(4,7)
		time.sleep(random_wait)
		pass
	try:
		websource = sel.get_html_source()
		# regex to get show all groups URL
		m = re.search('<a href="http://www.facebook.com/groups.php\?id=(.*?)">See All \((.*?)\)',websource,re.IGNORECASE)
		logging.info("userid: " + m.group(1))
		# user is member of #groups
		logging.info("groups: " + m.group(2))
		group_link = "http://www.facebook.com/groups.php?id=" + m.group(1)
		logging.info("group link: " + group_link)
		sel.open(group_link)
		random_wait = random.randint(3,6)
		time.sleep(random_wait)
		# for very weird reasons, the onclick command works only for every second link
		# so have to iterate the removal function couple of times
		# don't ask why, it took me 2hours to find out this annoyance
		for j in range(int(m.group(2))):
			websource = sel.get_html_source()
			# regex to find all remove group onclcik events
			m = re.findall('onclick=\'(return group_ask_leave\(".*?)\'',websource,re.IGNORECASE)
			logging.info(m)
			for i in m:
				click_link = "//a[@onclick='"+i+"']"
				try:
					sel.click(click_link)
					logging.info("clicked to remove group: " + click_link)
					random_wait = random.randint(3,5)
					time.sleep(random_wait)
					sel.click("remove")
					logging.info("removed da group: " + str(i))
					random_wait = random.randint(1,3)
					time.sleep(random_wait)
				except:
					logging.warning("couldn't remove group: " + i)
		logging.info("[ok] finished ungrouping")
	except:
		logging.info("[failed] apparently no groups to be removed")
	return sel

def delPosts(sel):
	logging.info("trying to delete wall posts")
	sel.click("link=Profile")
	random_wait = random.randint(5,9)
	time.sleep(random_wait)
	i = 0
	try:
		while (sel.is_element_present("//a[@class='UIIntentionalStory_Pic']")) == 1 :
			if(sel.is_element_present("//a[@class='PagerMoreLink']") == 1):
				sel.click("//a[@class='PagerMoreLink']")
			try:
				sel.click("//a[@class='UIButton UIButton_Gray UIActionButton_SuppressMargin UIButton_Suppressed UIActionButton']")
				random_wait = random.randint(2,4)
				time.sleep(random_wait)
				sel.click("delete_story")
				logging.info(str(i) + " post deleted")
				random_wait = random.randint(1,4)
				time.sleep(random_wait)
			except:
				logging.warning("deleting post failed")
				pass
			if (i % 20 == 0):
				sel.click("link=Profile")
				random_wait = random.randint(5,9)
				time.sleep(random_wait)
			i+= 1
	except:
		logging.info("deleting posts done")
		
	return sel

def addFriendFriend(sel,offset,depth,pages_start,pages_end):
	print "... launch anti-social friend shooter"
	#sel.click("link=All Friends")
	random_wait = random.randint(2,4)
	time.sleep(random_wait)
	# fetch all friend ID's from database
	filename = "myfriends.txt"
	reader = csv.reader(open(filename, "rb"))
	# parse em into list
	offset = int(offset)
	for row in reader:
		row.remove("") # remove last empty entry
	# create URL with ids
	for friends in row[offset:]:
		url_all_friends = "http://www.facebook.com/home.php?ref=home#/friends/?id=" + friends
		sel.open(url_all_friends)
		random_wait = random.randint(4,9)
		time.sleep(random_wait)

		try:
			for x in range(int(pages_start),int(pages_end)):
				link = "link=%d"%x
				sel.click(link)
				for i in range(0,int(depth)):
					sel.click("link=Add as Friend")
					time.sleep(3)
					random_wait = random.randint(1,4)
					if sel.is_visible("dialog_button1"):
						random_wait = random.randint(1,3)
						time.sleep(random_wait)
						try:
							sel.click("dialog_button1")
							time.sleep(1)
							try:
								sel.click("dialog_button1")
							except:
								pass
							try:
								sel.click("skip")
								random_wait = random.randint(2,5)
								time.sleep(random_wait)
							except:
								pass
						except:
							pass
				random_wait = random.randint(3,6)
				time.sleep(random_wait)
		except:
			pass
	return sel

# SAVE userinfo (name, profilepicture and amount of friends)
def getInfo(sel,lastwords,command,email,password):
	sel.open("http://www.facebook.com/profile.php")
	random_wait = random.randint(2,5)
	time.sleep(random_wait)
	capturepath = "/var/www/profiles/img/"
	filename = str(int(time.time())) + ".png"
	capture = capturepath + filename

	# get profile name and friends amount with regex-vodoo
	websource = sel.get_html_source()
	random_wait = random.randint(1,3)
	time.sleep(random_wait)
	try:
		m = re.search('<img id="profile_pic".*src="(.*?)\"/>',websource,re.IGNORECASE)
		profile_picture = m.group(1)
		logging.info("[ok] got the profile picture from " + username)
	except:
		try:
			m = re.search('<img src="(.*).?\"\salt=.*id="profile_pic">',websource,re.IGNORECASE)
			profile_picture = m.group(1)
			logging.info("[ok] got the profile picture from " + username)
		except:
			logging.warning("[failed] profile picture regex failed!!!")
			#logging.error(websource)
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
		logging.info("[ok] image cropped to 200px width")
	except:
		logging.error("[failed] image not cropped")
		pass
	try:
		m = re.search('<h1 id="profile_name">(.*)</h1>',websource,re.IGNORECASE)
		username = m.group(1)
		logging.info("[ok] username logged in as " + username)
		logging.info("[ok] " + username + " last words are " + lastwords)
	except:
		logging.warning("[failed] username regex failed!!!")
		pass
	try:
		m = re.search('<a.*?\">(\d*)\sfriends</a>',websource)
		#logging.info("websource is: " + websource)
		friends = m.group(1)
		logging.info("[ok] " + username + " has " + friends + " friends!")
	except:
		logging.warning("[failed] friendsamount regex failed!!!")
		friends = "n/a"
		pass
	# sql query

	try:
		q = "INSERT INTO web20suicide.users(`id`,`username`,`friends`,`picture`,`lastwords`,`command`,`t_create`,`email`,`password`) VALUES (NULL,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,%s,%s)"
		cursor.execute(q, (username,friends,filename,lastwords,command,email,password,))
		logging.info("[ok] user " + username + " added to mysql")
		try:
			time.sleep(2)
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



def removeFriends(sel,amount):
	sel.open("http://www.facebook.com/friends/")
	random_wait = random.randint(3,6)
	time.sleep(random_wait)
	sel.open("http://www.facebook.com/friends/?ref=tn#/friends/?filter=afp")
	time.sleep(4)
	websource = sel.get_html_source()
	time.sleep(1)
	if (amount == "n/a"):
		amount = "500"
	i = 1
	while (sel.is_element_present("//a[@class='UIPager_Button UIPager_ButtonForward']")) == 1:
		try:
			sel.click("//a[@class='UIObjectListing_RemoveLink']")
			random_wait = random.randint(2,4)
			time.sleep(random_wait)
			sel.click("remove")
			random_wait = random.randint(1,3)
			time.sleep(random_wait)
			logging.info("friend " + str(i) + " deleted")
			i += 1
		except:
			try:
				#sel.open("http://www.facebook.com/friends/?ref=tn#/friends/?filter=afp")
				sel.click("//a[@class='UIPager_Button UIPager_ButtonForward']")
				logging.info("friend 50 reached - flip page")
				random_wait = random.randint(4,6)
				time.sleep(random_wait)
				if (sel.is_element_present("//div[@class='UIObjectListing clearfix UIObjectListing_HasRemoveControl']")) == 0:
					logging.info("no more friends available")
					break
			except:
				logging.info("couldn't click the forward button")
				break
			pass
	try:
		logging.info("trying to reload friends page and kill 'em")

		sel.open("http://www.facebook.com/friends/")
		random_wait = random.randint(3,6)
		time.sleep(random_wait)
		sel.open("http://www.facebook.com/friends/?filter=ac")
		#sel.open("http://www.facebook.com/friends/?ref=tn#/friends/?filter=afp")
		time.sleep(9)
		websource = sel.get_html_source()
		time.sleep(1)
		while (sel.is_element_present("//a[@class='UIPager_Button UIPager_ButtonForward']")) == 1:
			try:
				sel.click("//a[@class='UIObjectListing_RemoveLink']")
				random_wait = random.randint(2,4)
				time.sleep(random_wait)
				sel.click("remove")
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				logging.info("friend " + str(i) + " deleted")
				i += 1
			except:
				try:
					sel.click("//a[@class='UIPager_Button UIPager_ButtonForward']")
					logging.info("friend 50 reached - flip page - clicked the forward button")
					random_wait = random.randint(4,6)
					time.sleep(random_wait)
					if (sel.is_element_present("//div[@class='UIObjectListing clearfix UIObjectListing_HasRemoveControl']")) == 0:
						logging.info("no more friends available")
						break
				except:
					logging.info("couldn't click the forward button")
					break
				pass
		sel.open("http://www.facebook.com/friends/")
		random_wait = random.randint(3,6)
		time.sleep(random_wait)
		sel.open("http://www.facebook.com/friends/?filter=ac")
		#sel.open("http://www.facebook.com/friends/?ref=tn#/friends/?filter=afp")
		time.sleep(9)
		websource = sel.get_html_source()
		time.sleep(1)
		while (sel.is_element_present("//a[@class='UIPager_Button UIPager_ButtonBack']")) == 1:
			try:
				sel.click("//a[@class='UIObjectListing_RemoveLink']")
				random_wait = random.randint(2,4)
				time.sleep(random_wait)
				sel.click("remove")
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				logging.info("friend " + str(i) + " deleted")
				i += 1
			except:
				try:
					sel.click("//a[@class='UIPager_Button UIPager_ButtonBack']")
					logging.info("friend 50 reached - flip page - clicked the backward button")
					random_wait = random.randint(4,6)
					time.sleep(random_wait)
					if (sel.is_element_present("//div[@class='UIObjectListing clearfix UIObjectListing_HasRemoveControl']")) == 0:
						logging.info("no more friends available")
						break
				except:
					try:
						sel.click("//a[@class='UIPager_Button UIPager_ButtonForward']")
						logging.info("friend 50 reached - flip page - clicked the forward button")
						random_wait = random.randint(4,6)
						time.sleep(random_wait)
						if (sel.is_element_present("//div[@class='UIObjectListing clearfix UIObjectListing_HasRemoveControl']")) == 0:
							logging.info("no more friends available")
							break
					except:
						logging.info("couldn't click the forward button")
						break
				pass
		time.sleep(5)
		websource = sel.get_html_source()
		time.sleep(1)
		while (sel.is_element_present("//a[@class='UIPager_Button UIPager_ButtonForward']")) == 1:
			try:
				sel.click("//a[@class='UIObjectListing_RemoveLink']")
				random_wait = random.randint(2,4)
				time.sleep(random_wait)
				sel.click("remove")
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				logging.info("friend " + str(i) + " deleted")
				i += 1
			except:
				try:
					sel.click("//a[@class='UIPager_Button UIPager_ButtonForward']")
					logging.info("friend 50 reached - flip page - clicked the forward button")
					random_wait = random.randint(4,6)
					time.sleep(random_wait)
					if (sel.is_element_present("//div[@class='UIObjectListing clearfix UIObjectListing_HasRemoveControl']")) == 0:
						logging.info("no more friends available")
						break
				except:
					logging.info("couldn't click the forward button")
					break
				pass
	except:
		logging.info("no more friends to be removed")
		pass

	#for i in range(1,int(amount)+1):
	#	try:
	#		try:
	#			try:
	#				sel.click("//a[@class='UIObjectListing_RemoveLink']")
	#				random_wait = random.randint(2,4)
	#				time.sleep(random_wait)
	#				sel.click("remove")
	#				random_wait = random.randint(1,3)
	#				time.sleep(random_wait)
	#				logging.info("friend " + str(i) + " deleted")
	#			except:
	#				pass
	#			# click forward button to enter next page of friend list after 50kills
	#			if (i % 50 == 0):
	#				sel.click("//a[@class='UIPager_Button UIPager_ButtonForward']")
	#				logging.info("friend 50 reached - flip page")
	#				random_wait = random.randint(4,6)
	#				time.sleep(random_wait)
	#	 	except:
	#	 		logging.error("something went wrong with friedn removal")
	#	 		pass
	#	except:
	#		logging.warning("[failed] friend couldn't be deleted! (perhaps overflow)")
	#		logging.warning("[bokito] now running penetration mode")
	#		try:
	#			for i in range(1,1000):
	#				sel.click("//a[@class='UIObjectListing_RemoveLink']")
	#				random_wait = random.randint(2,4)
	#				time.sleep(random_wait)
	#				sel.click("remove")
	#				random_wait = random.randint(1,3)
	#				time.sleep(random_wait)
	#				logging.info("friend " + str(i) + " deleted")
	#				# click forward button to enter next page of friend list after 50kills
	#				try:
	#					if (i % 50 == 0):
	#						sel.click("//a[@class='UIPager_Button UIPager_ButtonForward']")
	#						logging.info("friend 50 reached - flip page")
	#						random_wait = random.randint(4,6)
	#						time.sleep(random_wait)
	#				except:
	#					logging.error("something went wrong with friedn removal")
	#					pass
	#		except:
	#			pass
	return sel


def SearchaddFriends(sel,searchfor):
	#sel = login_process(name,password)
	print "... launch anti-social friend shooter"
	sel.type("q", searchfor)
	sel.click("//div[@id='universal_search_submit']/a/span")
	# old facebook
	#sel.type("q",searchfor)
	#sel.key_press("q","\\13") # press enter key
	#
	random_wait = random.randint(3,6)
	time.sleep(random_wait)
	captcha = "0"
	randiii = random.randint(3,4)

	for i in range(0,randiii):
		try:
			sel.click("link=Add as Friend")
			random_wait = random.randint(1,4)
			time.sleep(random_wait)
			if sel.is_visible("dialog_button1"):
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				sel.click("dialog_button1")
				time.sleep(1)

				time.sleep(2)
				try:
					sel.click("dialog_button1")
				except:
					pass
			time.sleep(2)
		except:
			print "pass the captcha test.."
	try:
		sel.click("link=Profile")
	except:
		pass
	random_wait = random.randint(3,6)
	time.sleep(random_wait)
	try:
		sel = change_status3(sel,searchfor)
		random_wait = random.randint(3,6)
		time.sleep(random_wait)
	except:
		pass
	return sel

def MightKnownFriends(sel):
	sel.click("//div[@id='fb_menu_home']/div/a/span")
	random_wait = random.randint(6,10)
	time.sleep(random_wait)
	try:
		sel.click("//div[@id='content']/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[5]/div[1]/div/a")
	except:
		sel.open("http://www.facebook.com/findfriends.php?expand=pymk&ref=hpb")
	random_wait = random.randint(3,7)
	time.sleep(random_wait)
	for i in range(0,150):
			random_wait = random.randint(2,6)
			time.sleep(random_wait)
			sel.click("link=Add as Friend")
			random_wait = random.randint(1,4)
			time.sleep(random_wait)
			if sel.is_visible("dialog_button1"):
				random_wait = random.randint(1,3)
				time.sleep(random_wait)
				sel.click("dialog_button1")
				time.sleep(1)

				time.sleep(2)
				try:
					sel.click("dialog_button1")
				except:
					pass
			time.sleep(2)
	return sel
