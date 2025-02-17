"""
__main__.py
Anna Chen
Created: 2025-01-30
Last Updated: 2025-02-08
 
This file is the starting point of the program.
It also contains the command-line interface logic for the task timer program.
"""

# import the TaskManager class which has all the important methods
# Use a relative import ".task_manager" to run the package as module with "python -m task_timer"
from .task_manager import TaskManager


def program_intro():
    """ Display program name and introduce available commands. """

    print("\n-------------------------------------------------------------------------------\n")
    print("                             Task Timer\n")
    print("  This is a command line interface program that allow the user to track")
    print("  multiple tasks at a time.")


def handle_commands():

    # Initialize the task dataframe
    task_manager = TaskManager()
    
    # Display program name and introduce available commands
    program_intro()
    task_manager.list_commands()

    while True:

        # prompt user input and change inout to all lower case for consistency
        user_input = input("\nEnter command: ")
        user_input = user_input.lower()

        # start new task
        if user_input == "1" or user_input == "start task":
            task_manager.start_task()

        # Display currently running tasks and end task according to user input
        elif user_input == "2" or user_input == "end task":
            task_manager.running_tasks()
            task_manager.end_task()

        elif user_input == "3" or user_input == "running tasks":
            task_manager.running_tasks()

        elif user_input == "5" or user_input == "export csv":
            task_manager.export_csv()

        elif user_input == "4" or user_input == "show task records" or user_input == "show task record":
            task_manager.show_records()

        elif user_input =="6" or user_input == "help":
            task_manager.list_commands()
        
        # exit program
        elif user_input == "7" or user_input == "exit":
            """
            Ask the user if they want to export records, then exit program.
            """
            print("  All task records will be deleted when program ends.")
            export_csv = input("  Do you want to export task records to a csv file? (Y/N) ")

            export_csv = export_csv.lower()

            if export_csv == "y" or export_csv == "yes":
                task_manager.export_csv()

            print("\n  Thanks for using this program. Bye.")
            print("---------------------------------------------------------------------------------")
            break
        
        # Handle invalid input
        else:
            print("\n      Error: Invalid command. Enter \"help\" to see available commands.")


def main():
    # Start the program and handle commands
    handle_commands()

if __name__ == '__main__':
    main()