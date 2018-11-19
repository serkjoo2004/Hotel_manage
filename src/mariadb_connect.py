import pymysql

# Open database connection
conn = pymysql.connect(host='localhost', port=3306, user='one', password='one111', db='hotel', charset='utf8')

# prepare a cursor object
curs = conn.cursor()

# execute SQL query
curs.execute("select version()")

# fetch a single row
data = curs.fetchone()

print("Database version : %s" %data)

# disconnect from server
conn.close()