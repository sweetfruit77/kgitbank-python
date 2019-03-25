import MySQLdb

# Open database connection
db = MySQLdb.connect(host='127.0.0.1',user='root',\
    password='qwer1324',database='test',port=3306)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()
