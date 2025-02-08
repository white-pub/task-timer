"""
functions.py
Anna Chen

Created: 2025-02-07
Last Updated: 2025-02-07

This file contains the functions needed for the task timer program.
"""

import pandas as pd
from datetime import datetime

class TaskManager:
    def __init__(self):
        # Create a pandas dataframe to store task details.
        self.df = pd.DataFrame(columns=["Task ID", "Task name", "Start time", "End time", "duration"])
        self.current_id = 0

    def start_task(self):
        """
        Start a task timer and assign the task a unique ID number.
        Prompt for optionl task name.
        """
        
        # assign unique ID for task
        self.current_id = self.current_id + 1

        # capture current time, include month, date, hour, minute, second
        current_time = datetime.now()
        formatted_time = current_time.strftime("%m-%d %H:%M:%S")

        # Prompt task name from user, defult is a blank space
        task_name = input("  Task name (optinal):")
        if task_name == "":
            task_name = " "
        
        # Create new entry and append to dataframe
        new_row = {"Task ID": self.current_id,"Task name": task_name,"Start time": formatted_time, "End time": "Still running", "duration": " "}
        self.df = self.df.append(new_row, ignore_index=True)

        print(f"  Task timer has started. Task ID: {self.current_id}. Task name: {task_name}")


    def list_commands(self):

        commands = """
        Available command and its explanations:
        - start task
            This will start a new task timer, the system will assign a unique ID for the task.
            The prompt "task name (optional):" will appear, the user can enter a task name or just press "ENTER" to leave it blank.
        - running tasks
            This will display the tasks that are currently running.
        - end task XXX
            The XXX will be the ID number of the task the user wish to end.
        - show task record
            All the task records will be shown, including task ID, task name, start time, end time, and duration.
        - export csv
            The task records will be exported as a CSV file, with the file name task_timer_record_XXXXXXXX.csv
            The string of XXXXXXXX will be the date and time the file was created, in the format mm/dd/hh/mm, with 24-hour notation.
            For example, a file exported at Feb 7th 6:35pm will be "task_timer_record_02071835.csv"
        - help
            This will display a list of commands the user can use, with explanations.
        - exit
            This will exit the task timer program. A prompt will appear to ask the user if they want to export the records as CSV

        Note: 
        1. The commands can be upper case or lower case. 
        2. Time format for each task is mm-dd hh:mm:ss, using the 24-hour notation. For example, May 2nd 2:30:10 pm will be stored as "05-05 14:30:10"
        """

        print(commands)

        # task_duration = datetime.now() - start_time