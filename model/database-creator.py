import sqlite3

def CreateDatabase():
    db = sqlite3.connect('bug-tracker-db.db')
    db.execute('CREATE TABLE BUGTRACKER (BUG_ID INT PRIMARY KEY,BUG_NAME VARCHAR NOT NULL, BUG_SECTION INT NOT NULL,DESCRIPTION VARCHAR, IMPORTANCE INT NOT NULL,PROJECT_NAME INT NOT NULL);')
    #db.execute('CREATE TABLE DATE (BUG_ID INT')
CreateDatabase()