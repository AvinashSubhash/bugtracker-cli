import os
import time
from model import database_handler
from controller import data_manipulator
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
    time.sleep (2)
    while True:
        print("Main Menu:")
        print("\n 1. Add a bug\n 2. View all bugs\n 3. Modify a bug\n\nOption:",end='')
        num = int(input())
        if num == 1:
            control.AddData()
        elif num == 2:
            control.DisplayData()
        elif num == 3:
            os.system('clear')
            control.ModifyData()
        else:
            os.system('clear')
            print("\n Invalid Option!! \n")
    break

