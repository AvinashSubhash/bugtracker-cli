
import time
from datetime import date
import os 
from model import database_handler
class DataManipulation:

    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0#str(time.localtime()[2])
        self.hour = 0#str(time.localtime()[3])
        self.minute = 0#str(time.localtime()[4])
        self.seconds = 0#str(time.localtime()[5])
        self.db = 0
        #print(self.seconds)

    def CalculateID(self):
        self.year = str(time.localtime()[0])
        self.month = str(time.localtime()[1])
        self.day = str(time.localtime()[2])
        self.hour = str(time.localtime()[3])
        self.minute = str(time.localtime()[4])
        self.seconds = str(time.localtime()[5])

    def InitializeTables(self):
        self.db = database_handler.DatabaseHandler()
        self.db.CreateDatabase()

    def IDGenerattor(self):
        key =''
        self.CalculateID()
        if int(self.seconds) < 10:
            key += '0'
        key += self.seconds
        if int(self.hour) < 10:
            key += '0'
        key += self.hour
        if int(self.day) < 10:
            key += '0'
        key += self.day
        if int(self.month) < 10:
            key += '0'
        key += self.month
        if int(self.year) < 10:
            key += '0'
        key += self.year
        if int(self.minute) < 10:
            key += '0'
        key += self.minute

        return key

    def CalculateDateDifference(self,old_date,current_date):
        old_date_i = date(int(old_date[2]),int(old_date[1]),int(old_date[0]))
        new_date_i = date(int(current_date[0]),int(current_date[1]),int(current_date[2]))
        diff = new_date_i - old_date_i
        return diff.days


    def OpeningDate(self):
        return ""+str(time.localtime()[2])+"-"+str(time.localtime()[1])+"-"+str(time.localtime()[0])

    def UpdateDatabase(self):
        self.db = database_handler.DatabaseHandler()
        data_set = []
        [_,data] = self.db.GetData()
        self.CalculateID()
        current_date = [self.year,self.month,self.day]
        for i in range(len(data)):
            if data[i][2] == '-':
                temp = data[i][1].split('-')
                days = self.CalculateDateDifference(temp,current_date)
                temp.append(days)
                temp.append(data[i][0])
                data_set.append(temp)

        self.db.UpdateDatabase(data_set)

    def DisplayNames(self):
        file1 = open('controller/name_to_index.txt','r')
        [projectnames,bugsection] = file1.readlines()
        projectnames = projectnames.split(' ')
        bugsection = bugsection.split(' ')
        print("Project names:")
        for i in projectnames:
            print(i)
        print("Bug Sections:")    
        for i in bugsection:
            print(i)
    
    def NameToIndex(self,projectname, bugsection):
        final_data=[]
        print("Projectname:",projectname)
        print("Bugsection:",bugsection)
        file1 = open('controller/name_to_index.txt','r')
        [projectnames,bugsections] = file1.readlines()
        file1.close()

    def DisplayData(self):
        os.system('clear')
        [data_1,data_t] = self.db.GetData()
        if len(data_1) > 0:
            data_3=0
            for i in range(len(data_1)):
                data_2 = data_1[i]
                for j in data_t:
                    if j[0] == data_2[0]:
                        data_3 = j
                
                print("\nBug ID: ",data_2[0],"    ",end='')
                print("Bug Name: ",data_2[1])
                print("Bug Section: ",data_2[2])
                print("Description: ",data_2[3])
                print("Importance:  ",data_2[4])
                print("Project Name:",data_2[5])
                print("Opening Date:",data_3[1])
                print("Closing Date: ",data_3[2])
                print("No. of Days Active: ",data_3[3],"\n")
            print("*************************\n")
        else:
            print("Empty Database. .")
        #will take raw data from database and then display it in a table format.

    def AddData(self,data_list):
        #self.NameToIndex(data_list[1],data_list[2])
        data_list.append(self.IDGenerattor())
        data_list.append(self.OpeningDate())
        data_list.append('-')
        data_list.append(0)
        self.db.InsertData(data_list)
        #will change the data type into appropriate format and pass it to datbase handler

    def ModifyData(self,data_index,data_value,id):
        self.db.ModifyData(data_index,data_value,id)

    def CheckEntry(self,bug_id):
        if bug_id in self.db.CheckEntry():
            return True
        return False
    
    def CloseConnection(self):
        self.db.Disconnect()
        
    


sp = DataManipulation()
print(sp.IDGenerattor())




