import MySQLdb,sys

def connect_db():
	host_name = "localhost"
	user_name ="killer"
	password ="killer"
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
