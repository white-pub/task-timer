"""
cli.py
Anna Chen

Created: 2025-02-07
Last Updated: 2025-02-07

This file contains the command-line interface logic for the task timer program.
"""
# import the TaskManager class which has all the important methods
from functions import TaskManager

def main():

    # Initialize the task dataframe
    task_manager = TaskManager()

    # Display program name and introduce available commands
    print("\n-----------------------------------------------\n")
    print("                Task Timer\n")
    print("  This is a command line interface program that allow the user to ")
    print("  track multiple tasks at a time.")
    task_manager.list_commands()




    while True:

        # prompt user input and change inout to all lower case for consistancy
        user_input = input("Enter command:")
        user_input = user_input.lower()

        # start new task
        if user_input == "start task":
            task_manager.start_task()

        elif user_input == "help":
            task_manager.list_commands()
        
        # exit program
        elif user_input == "exit":
            break
        
        # Handle invalid input
        else:
            print("Invalid command.")
            task_manager.list_commands()


