import MySQLdb,sys

def connect_db():
#host_name = "mysqlsvr10.world4you.com"
#	user_name ="yugoat"
#	password ="7jx9t"
#	db_name="yugoatdb6"
	host_name = "localhost"
	user_name ="gordo"
	password ="mockshow"
	db_name="web20suicide"

	try:
		conn = MySQLdb.connect (db = db_name,
																		host = host_name,
																		user = user_name,
																		passwd = password)
		return conn

	except MySQLdb.Error, e:
		print "Cannot connect to server"
		print "Error code:", e.args[0]
		print "Error message:", e.args[1]
		sys.exit(1)
