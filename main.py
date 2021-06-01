import os
from model import database_creator
while True:

    count=0
    os.system('clear')
    #path = os.getcwd()
    print("BUGTRACKER-CLI v1.0")
    print("")
    print("Current Databases:")
    files = list(os.listdir('model'))
    if 'bug-tracker.db' not in files:
        print("")
        print("Initializing Database. . .")
        
    else:
        print('')
        print("Updating Database. . .")
    break

