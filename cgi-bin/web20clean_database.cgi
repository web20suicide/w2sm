#!/usr/bin/python

from selenium import selenium
import settings,MySQLdb

# global settings
dbconn = settings.connect_db()
cursor = dbconn.cursor(MySQLdb.cursors.DictCursor)

print "Content-type: text/html"
print 

q = "DELETE FROM web20suicide.friendbot"
cursor.execute(q,)


print "ok"
