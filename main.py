import os
import time
from controller import data_manipulator
from graphics import Graphics
#print('*')
control = data_manipulator.DataManipulation()
def GetDetails():
    data1=[]
    while len(data1) !=4 :
        #os.system('clear')
        Graphics.DisplayGraphics()
        print("Enter the following data:\n")
        data1.append(input("Bug Name:"))
        data1.append(input("Project Name:"))
        data1.append(input("Bug Section:"))
        data1.append(input("Importance (Only integer values between 1 and 5) :"))
        data1.append(input("Description:"))
        Graphics.DisplayGraphics()
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
    
    #print('*')
    Graphics.DisplayGraphics()
    files = list(os.listdir('model'))
    if 'bug-tracker.db' in files:
        print('')
        print("Updating Database. . .")
        control.UpdateDatabase()
        print('')
        #print('*')
    else:
        #print('*')
        print("")
        print("Initializing Database. . .")
        control.InitializeTables()
    while True:
        print("Main Menu:")
        print("\n 1. Add a bug\n 2. View all bugs\n 3. Modify a bug\n 4. Close a bug\n 5. Exit\n\n>",end='')
        try:
            num = int(input())
        except:
            #os.system('clear')
            Graphics.DisplayGraphics()
            print('\033[91m'+"Input Error . ."+'\033[0m'+"\n")
        if num == 1:
            try:
                control.AddData(GetDetails())
            except:
                #os.system('clear')
                Graphics.DisplayGraphics()
                print('\033[91m'+"Input Error . ."+'\033[0m'+"\n")
        elif num == 2:
            control.DisplayData()
        elif num == 3:
            control.ModifyData()
        elif num == 4:
            control.CloseBug()
        elif num == 5:
            control.CloseConnection()
            os.system('clear')
            exit(0)
        else:
            #os.system('clear')
            Graphics.DisplayGraphics()
            #control.DisplayNames()
            print('\033[91m'+"Invalid Option . ."+'\033[0m'+"\n")
    break

