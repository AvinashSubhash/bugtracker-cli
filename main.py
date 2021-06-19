import os
import time
from controller import data_manipulator
#print('*')
control = data_manipulator.DataManipulation()
def GetDetails():
    data1=[]
    while len(data1) !=4 :
        os.system('clear')
        print("Enter the following data:\n")
        data1.append(input("Bug Name:"))
        data1.append(input("Project Name:"))
        data1.append(input("Bug Section:"))
        data1.append(input("Importance:"))
        data1.append(input("Description:"))
        flag=0
        #print(data1)
        for i in data1:
            if len(i) == 0: 
                flag=1
        if flag == 1:
            print("\nInvalid Data Entry! Please enter again!")
            time.sleep(2)
                
        if flag == 0:
            break
    return data1

#print('*')
db = 0
while True:

    count=0
    os.system('clear')
    #path = os.getcwd()
    print("BUGTRACKER-CLI v1.0")
    #print('*')

    files = list(os.listdir('model'))
    if 'bug-tracker.db' not in files:
        print("")
        print("Initializing Database. . .")
        control.InitializeTables()
        #print('*')
    else:
        
        #print('*')
        print('')
        print("Updating Database. . .")
        control.UpdateDatabase()
        print('')
    while True:
        print("Main Menu:")
        print("\n 1. Add a bug\n 2. View all bugs\n 3. Modify a bug\n 4. Exit\n\n>",end='')
        try:
            num = int(input())
        except:
            os.system('clear')
            print("Invalid Entry!")
        if num == 1:
            try:
                control.AddData(GetDetails())
            except:
                os.system('clear')
                print("Input Error. .\n")
        elif num == 2:
            control.DisplayData()
        elif num == 3:
            os.system('clear')
            print("Column names: ")
            print("1:BUGNAME      2:BUG_SECTION    3:DESCRIPTION")
            print("4:IMPORTANCE   5:PROJECT_NAME   6:CLOSING_DATE")
            print("\n\nEnter the BUG_ID of the entry:")
            #try:
            bug_id=int(input())
            if control.CheckEntry(bug_id):
                print("\n\nEnter the index number of column to be edited:")
                data_index = input().split(' ')
                data_index = [int(i) for i in data_index]
                print("Enter the data in appropriate format ans spaces:")
                data_value = input().split(' ')
                control.ModifyData(data_index,data_value,bug_id)
            else:
                print("Sorry. . no such entry found :-(")
                time.sleep(3)
                os.system('clear')
            #except:
            #    os.system('clear')
            #    print("Input Error. .")
        elif num == 4:
            control.CloseConnection()
            os.system('clear')
            exit(0)
        else:
            os.system('clear')
            #control.DisplayNames()
            print("\n Invalid Option!! \n")
    break

