import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="SGRUDErokx2k20",database="marks")
mycursor=mydb.cursor()
mycursor.execute("show tables")
