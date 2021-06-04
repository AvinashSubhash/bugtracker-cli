import os
import time
from model import database_handler
from controller import data_manipulator

def GetDetails():
    data1=[]
    while len(data1) !=4 :
        os.system('clear')
        print("Enter the details in the given format with spaces [BugName ProjectName BugSection Importance] ")
        data1 = input().split(' ')
        print("Enter the description for the bug:")
        data2 = input()
        #print(data1)
        if len(data1) != 4:
            print("Invalid Data Entry! Please enter again!")
            time.sleep(2)
        else:
            data1.append(data2)
            break
    return data1


while True:

    count=0
    os.system('clear')
    #path = os.getcwd()
    control = data_manipulator.DataManipulation()
    print("BUGTRACKER-CLI v1.0")


    files = list(os.listdir('model'))
    if 'bug-tracker.db' not in files:
        print("")
        print("Initializing Database. . .")
        db = database_handler.DatabaseHandler()
        db.CreateDatabase()
    else:
        print('')
        print("Updating Database. . .")
        control.UpdateDatabase()
        print('')
    while True:
        print("Main Menu:")
        print("\n 1. Add a bug\n 2. View all bugs\n 3. Modify a bug\n\nOption:",end='')
        try:
            num = int(input())
        except:
            print("Invalid Entry!")
        if num == 1:
            control.AddData(GetDetails())
        elif num == 2:
            control.DisplayData()
        elif num == 3:
            os.system('clear')
            control.ModifyData()
        else:
            os.system('clear')
            print("\n Invalid Option!! \n")
    break
