import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "root",
    database = "ehis"
)
db = mydb.cursor()
db.execute("select * from academicyears")
for x in db:
    print(x)
   # db.execute("select * from academicyears")