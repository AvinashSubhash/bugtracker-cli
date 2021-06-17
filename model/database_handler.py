import sqlite3
import time

class DatabaseHandler:

    def __init__(self):
        #print("DatabaseHandler init function accessed . .")
        self.db = sqlite3.connect('model/bug-tracker.db')
        self.column_list = ['BUG_ID','BUG_NAME','BUG_SECTION','DESCRIPTION','IMPORTANCE','PROJECT_NAME','CLOSING_DATE']

    def CreateDatabase(self):
    
        self.db.execute('CREATE TABLE BUGTRACKER (BUG_ID INT PRIMARY KEY,BUG_NAME VARCHAR NOT NULL, BUG_SECTION INT NOT NULL,DESCRIPTION VARCHAR, IMPORTANCE INT NOT NULL,PROJECT_NAME INT NOT NULL);')
        self.db.execute('CREATE TABLE DATE (BUG_ID INT NOTL NULL, OPENING_DATE REAL NOT NULL, CLOSING_DATE REAL NOT NULL,NO_DAYS INT NOT NULL, FOREIGN KEY (BUG_ID) REFERENCES BUGTRACKER (BUG_ID));')
        print('\n---database creation successful---\n')
    
    def GetData(self):
        
        data = self.db.execute('SELECT * FROM BUGTRACKER;')
        data2 = self.db.execute('SELECT * FROM DATE;')
        return [data.fetchall(),data2.fetchall()]

    def InsertData(self,data):
        
        #print("Database Handler Insert function accessed. .")
        print(data)
        #try:
        string1 = str("INSERT INTO BUGTRACKER VALUES("+str(data[5])+", '"+str(data[0])+"', "+str(2)+", '"+str(data[4])+"', "+str(5)+", '"+str(data[1])+"');")
        #print(string1)
        string2 = str("INSERT INTO DATE VALUES("+str(data[5])+", '"+str(data[-3])+"', '"+str(data[-2])+"', "+str(0)+");")
        print(string2)
        #time.sleep(5)
        self.db.execute(string1)
        self.db.execute(string2)
            
        #except:
        #    print("Data could not be added. .")

    def UpdateDatabase(self):
        pass
        #print("Default modifier function for changing dated and values")  

    def CheckEntry(self):
        string1="SELECT BUG_ID FROM BUGTRACKER;"
        data1 = self.db.execute(string1)
        return list(data1.fetchall()[0]) 
    
    def ModifyData(self,data_index,data_value,id):
        #print("Database Handler Modify function accessed. .")
        print("Data Index: ",data_index)
        print("Data Values: ",data_value)
        self.db.execute("")


    def Disconnect(self):
        self.db.commit()
        self.db.close()

