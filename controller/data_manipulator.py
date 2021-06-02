
import time 
class DataManipulation:

    def __init__(self):
        self.year = str(time.localtime()[0])
        self.month = str(time.localtime()[1])
        self.day = str(time.localtime()[2])
        self.hour = str(time.localtime()[3])
        self.minute = str(time.localtime()[4])
        self.seconds = str(time.localtime()[5])
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

    def UpdateDatabase(self):
        pass

sp = DataManipulation()
print(sp.IDGenerattor())




