import sqlite3
import time
import os

class DatabaseHandler:

    def __init__(self):
        #print("DatabaseHandler init function accessed . .")
        self.db = sqlite3.connect('model/bug-tracker.db')
        self.column_list = ['BUG_ID','BUG_NAME','BUG_SECTION','DESCRIPTION','IMPORTANCE','PROJECT_NAME','CLOSING_DATE']

    def CreateDatabase(self):
    
        self.db.execute('CREATE TABLE BUGTRACKER (BUG_ID INT PRIMARY KEY,BUG_NAME VARCHAR NOT NULL, BUG_SECTION REAL NOT NULL,DESCRIPTION VARCHAR, IMPORTANCE INT NOT NULL,PROJECT_NAME INT NOT NULL);')
        self.db.execute('CREATE TABLE DATE (BUG_ID INT NOTL NULL, OPENING_DATE REAL NOT NULL, CLOSING_DATE REAL NOT NULL,NO_DAYS INT NOT NULL, FOREIGN KEY (BUG_ID) REFERENCES BUGTRACKER (BUG_ID));')
        print('\n---database creation successful---\n')
    
    def GetData(self):
        
        data = self.db.execute('SELECT * FROM BUGTRACKER;')
        data2 = self.db.execute('SELECT * FROM DATE;')
        return [data.fetchall(),data2.fetchall()]

    def InsertData(self,data):
        
        #print("Database Handler Insert function accessed. .")
        print(data)
        try:
            string1 = str("INSERT INTO BUGTRACKER VALUES("+str(data[5])+", '"+str(data[0])+"', '"+str(data[2])+"', '"+str(data[4])+"', "+str(data[3])+", '"+str(data[1])+"');")
            #print(string1)
            string2 = str("INSERT INTO DATE VALUES("+str(data[5])+", '"+str(data[-3])+"', '"+str(data[-2])+"', "+str(0)+");")
            #print(string2)
            #time.sleep(5)
            self.db.execute(string1)
            self.db.execute(string2)
            
        except:
            os.system('clear')
            print("Data could not be added. .")

    def UpdateDatabase(self,data_set):
        for i in range(len(data_set)):
            string4 = str('UPDATE DATE SET NO_DAYS = '+str(data_set[i][3])+' WHERE BUG_ID = '+str(data_set[i][4])+';')
            #print(string4)
            self.db.execute(string4)
        self.db.commit()
        #print("Default modifier function for changing dated and values")  

    def CheckEntry(self):
        string1="SELECT BUG_ID FROM BUGTRACKER;"
        data1 = self.db.execute(string1)
        return list(data1.fetchall()[0]) 
    
    def ModifyData(self,data_index,data_value,id):
        #print("Database Handler Modify function accessed. .")
        for i in range(len(data_index)):
            if data_index[i] <= 5:
                string3 = str("UPDATE BUGTRACKER SET "+str(self.column_list[int(data_index[i])])+" = '"+str(data_value[i])+"' WHERE BUG_ID = "+str(id)+";")
                print(string3)
                self.db.execute(string3)
            else:
                string3 = str("UPDATE DATE SET "+str(self.column_list[int(data_index[i])])+" = '"+str(data_value[i])+"' WHERE BUG_ID = "+str(id)+";")
                print(string3)
                self.db.execute(string3)
        self.db.commit()
        #print("Data Index: ",data_index)
        #print("Data Values: ",data_value)
        self.db.execute("")


    def Disconnect(self):
        self.db.commit()
        self.db.close()

