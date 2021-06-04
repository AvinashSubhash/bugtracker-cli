
import time 
from model import database_handler
class DataManipulation:

    def __init__(self):
        self.year = str(time.localtime()[0])
        self.month = str(time.localtime()[1])
        self.day = str(time.localtime()[2])
        self.hour = str(time.localtime()[3])
        self.minute = str(time.localtime()[4])
        self.seconds = str(time.localtime()[5])
        self.db = database_handler.DatabaseHandler()
        #print(self.seconds)

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
        print("Data Manipulator Update Database Function Accessed. .")
        self.db.ModifyData()


    def DisplayData(self):
        self.db.GetData()
        #will take raw data from database and then display it in a table format.
    def AddData(self,data_list):
        data_list.append(self.IDGenerattor())
        data_list.append(self.OpeningDate())
        data_list.append('-')
        data_list.append(0)
        self.db.InsertData(data_list)
        #will change the data type into appropriate format and pass it to datbase handler
    def ModifyData(self):
        self.db.ModifyData()
        
        


sp = DataManipulation()
print(sp.IDGenerattor())




