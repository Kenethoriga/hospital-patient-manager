import PyMySQL
# Open database connection
db = PyMySQL.connect("localhost","root","Collymore1#","PATIENTS.sql" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)
# disconnect from server
db.close()
