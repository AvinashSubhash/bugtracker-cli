import sqlite3

class DatabaseHandler:

    def __init__(self):
        self.db = sqlite3.connect('model/bug-tracker.db')

    def CreateDatabase(self):
    
        self.db.execute('CREATE TABLE BUGTRACKER (BUG_ID INT PRIMARY KEY,BUG_NAME VARCHAR NOT NULL, BUG_SECTION INT NOT NULL,DESCRIPTION VARCHAR, IMPORTANCE INT NOT NULL,PROJECT_NAME INT NOT NULL);')
        self.db.execute('CREATE TABLE DATE (BUG_ID INT NOTL NULL, OPENING_DATE REAL NOT NULL, CLOSING_DATE REAL NOT NULL,NO_DAYS INT NOT NULL, FOREIGN KEY (BUG_ID) REFERENCES BUGTRACKER (BUG_ID));')
        print('--database creation successful---')
    def GetData(self):
        
        data = self.db.execute('SELECT * FROM BUGTRACKER;')
        return data.fetchall()

    def InsertData(self,data):
        print("Database Handler Insert function accessed. .")
        print(data)
        #try:
        string1 = str("INSERT INTO BUGTRACKER VALUES("+str(data[5])+", '"+str(data[0])+"', "+str(2)+", '"+str(data[4])+"', "+str(5)+", '"+str(data[1])+"');")
        print(string1)
        self.db.execute(string1)
        """except:
            print("Data could not be added. .")"""
    def ModifyData(self):
        print("Database Handler Modify function accessed. .")


