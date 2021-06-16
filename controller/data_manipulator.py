
import time
import os 
from model import database_handler
class DataManipulation:

    def __init__(self):
        self.year = str(time.localtime()[0])
        self.month = str(time.localtime()[1])
        self.day = str(time.localtime()[2])
        self.hour = str(time.localtime()[3])
        self.minute = str(time.localtime()[4])
        self.seconds = str(time.localtime()[5])
        self.db = 0
        #print(self.seconds)

    def InitializeTables(self):
        self.db = database_handler.DatabaseHandler()
        self.db.CreateDatabase()

    def IDGenerattor(self):
        key =''
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

    def OpeningDate(self):
        return ""+str(time.localtime()[2])+"-"+str(time.localtime()[1])+"-"+str(time.localtime()[0])

    def UpdateDatabase(self):
        self.db = database_handler.DatabaseHandler()
        #print("Data Manipulator Update Database Function Accessed. .")
        self.db.UpdateDatabase()

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
        """file1 = open('controller/name_to_index.txt','w')
        file1.seek(0,0)
        projectnames = projectnames.split(' ')
        bugsections = bugsections.split(' ')
        pn=''
        for i in projectnames:
            pn += i
            pn += ' '
        bs=''
        for i in bugsections:
            bs += i
            bs += ' '
        if projectname not in projectnames:
            print("New Project Identified, Adding to List. . .")
            pn += str(projectname)
        if bugsection not in bugsections:
            print("New Bug Section Identified, Adding to list. . .")
            bs += str(bugsection)
        file1.write(str(pn)+"\n"+str(bs))
        file1.close()"""


    def DisplayData(self):
        os.system('clear')
        data_1 = self.db.GetData()
        if len(data_1) > 0:
            data_1 = data_1[0]
            print("BUG_ID: ",data_1[0],"    ",end='')
            print("BUG_NAME: ",data_1[1])
            print("BUG_SECTION: ",data_1[2])
            print("DESCRIPTION: ",data_1[3])
            print("IMPORTANCE:  ",data_1[4])
            print("PROJECT_NAME:",data_1[5])
        print("Empty Database. .")
        print("")
        print("")
        #will take raw data from database and then display it in a table format.

    def AddData(self,data_list):
        self.NameToIndex(data_list[1],data_list[2])
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




