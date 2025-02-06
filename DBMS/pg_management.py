import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="root",
    db="pg_management"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Test the connection by executing a query
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print("Database version:", version)

# Close the connection
db.close()



