# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# ELeggett,11.15.2021,Added code to template
# ELeggett,11.16.2021,Debugged code
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt" # An object that represents a file
objFile = open(strFile, "a") # Opens/creates companion .txt file
lstData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """
    Menu of Options:\n
    \t1) Show current data
    \t2) Add a new item
    \t3) Remove an existing item
    \t4) Save data to file
    \t5) Exit program
    """   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionary rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstData = row.split(",")
    dicRow = {"Task": lstData[0].strip(), "Priority": lstData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
    print()  # Adds a new line for readability
    # Step 3 - Show the current items in the table
    if strChoice.strip() == "1":
        print("To Do List [Task (Priority)]:\n")
        for row in lstTable:
            print(row["Task"] + " ("+row["Priority"] + ")")
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == "2":
        strTask = input("Enter a task to add to your to do list: ")
        strPriority = input("Assign a priority (low, medium, or high): ")
        dicRow = {"Task": strTask.lower(), "Priority": strPriority.lower()}
        lstTable.append(dicRow)
        print("\nTask added to list!")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == "3":
        print("To Do List [Task (Priority)]:\n")
        for row in lstTable:
            print(row["Task"] + " (" + row["Priority"] + ")")
        strRemove = input("\nEnter a task to remove from your to do list: ")
        blnFlag = False
        intRow = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task.lower() == strRemove.lower():
                lstTable.remove(row)
                blnFlag = True
            intRow += 1
        if blnFlag == True:
            print("\nTask successfully removed from list!\n")
            print("To Do List [Task (Priority)]:\n")
            for row in lstTable:
                print(row["Task"] + " (" + row["Priority"] + ")")
        else:
            input("\nTask not found. Press Enter to return to main menu.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == "4":
        print("To Do List [Task (Priority)]:\n")
        for row in lstTable:
            print(row["Task"] + " (" + row["Priority"] + ")")
        strSave = input("\nSave current list to file? This can't be undone! (y/n): ")
        if strSave.lower() == "y":
            objFile = open(strFile, "w")
            for row in lstTable:
                objFile.write(row["Task"] + ", " + row["Priority"] + "\n")
            objFile.close()
            input("\nData saved to file. Press Enter to return to program.")
        else:
            input("\nData not saved to file. Press Enter to return to program.")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == "5":
        print("Closing list and exiting program. Goodbye!")
        objFile.close()
        break  # Exits the program
    else:
        print("Choose an option between 1 and 5!")
