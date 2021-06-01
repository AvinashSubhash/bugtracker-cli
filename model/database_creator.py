import sqlite3

class DatabaseHandler:

    def __init__(self):
        self.db = sqlite3.connect('bug-tracker.db')

    def CreateDatabase(self):
    
        self.db.execute('CREATE TABLE BUGTRACKER (BUG_ID INT PRIMARY KEY,BUG_NAME VARCHAR NOT NULL, BUG_SECTION INT NOT NULL,DESCRIPTION VARCHAR, IMPORTANCE INT NOT NULL,PROJECT_NAME INT NOT NULL);')
        self.db.execute('CREATE TABLE DATE (BUG_ID INT NOTL NULL, OPENING_DATE REAL NOT NULL, CLOSING_DATE REAL NOT NULL,NO_DAYS INT NOT NULL, FOREIGN KEY (BUG_ID) REFERENCES BUGTRACKER (BUG_ID));')

    def GetData(self):
        
        data = self.db.execute('SELECT * FROM DATE;')
        return data.fetchall()

