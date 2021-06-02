import os
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
        print('')
        #db.GetData()
    break

