import sqlite3

def CreateDatabase():
    db = sqlite3.connect('bug-tracker-db.db')
    db.execute('CREATE TABLE BUGTRACKER (BUG_ID INT PRIMARY KEY,BUG_NAME CHAR(20) NOT NULL, BUG_SECTION INT NOT NULL,DESCRIPTION CHAR(100), IMPORTANCE INT NOT NULL,PROJECT_NAME INT NOT NULL);')
    #print(db.execute('.schema BUGTRACKER'))

CreateDatabase()