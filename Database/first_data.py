import pymysql as mq
myobj = mq.connect(host="localhost",username="root",password="Anurag@mysql1")
cursorobj = myobj.cursor()
try:
    db = "Created database school"
    cursorobj.execute(db)
    print("database created")
except:
    print("database error ...")

