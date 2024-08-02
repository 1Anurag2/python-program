import mysql.connector
conn_obj = mysql.connector.connect(host="localhost", user="root", password="Anurag@mysql1", database="mydatabase")
  
# # creating the cursor object    
mycursor = conn_obj.cursor()  
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

  
