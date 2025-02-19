"""
task_manager.py
Anna Chen

Created: 2025-02-07
Last Updated: 2025-02-08

This file contains the TaskManager class which has the functions needed for the task timer program.
"""

import pandas as pd
from datetime import datetime

class TaskManager:
    def __init__(self):
        # Create a pandas dataframe to store task details.
        self.df = pd.DataFrame(columns=["Task ID", "Task name", "Start time", "End time", "Duration"])
        self.current_id = 0

    def start_task(self):
        """
        Start a task timer and assign the task a unique ID number.
        Prompt for optional task name.
        """
        
        # assign unique ID for task
        self.current_id = self.current_id + 1

        # capture current time, include month, date, hour, minute, second
        time_format = "%m-%d %H:%M:%S"
        current_time = datetime.now()
        formatted_time = current_time.strftime(time_format)

        # Prompt task name from user, default is a blank space
        task_name = input("\n  Task name (optional): ")
        if task_name == "":
            task_name = " "
        
        # Create new entry and add to dataframe using .loc 
        # Note: .append() is now deprecated, will cause error
        # new_task_info = {"Task ID": self.current_id,"Task name": task_name,"Start time": formatted_time, "End time": "Still running", "duration": " "}
        new_task_info = [self.current_id, task_name, formatted_time, "Still running", " "]
        self.df.loc[len(self.df)] = new_task_info
        # self.df = self.df.append(new_task_info, ignore_index=True)

        print(f"  Task timer has started. Task ID: {self.current_id}. Task name: {task_name}")

    def end_task(self):
        """
        Accepts one task ID, adds in end time and calculates duration.
        """

        # capture current time, include month, date, hour, minute, second
        time_format = "%m-%d %H:%M:%S"
        current_time = datetime.now()
        formatted_time = current_time.strftime(time_format)

        # Prompt for Task Id to end and handle value error
        task_id = input("\n  Please enter one task ID you want to end: ")
        try:
            task_id = int(task_id)
        except ValueError:
            print("\n  Error: You did not enter a valid number.")

        # Check if the ID is in range
        if task_id in self.df["Task ID"].values:
            task_row_index = task_id -1
            
            # Check if the task has already ended
            if self.df.loc[task_row_index, "End time"] == "Still running":
                # Update the task with the end time
                self.df.loc[task_row_index, "End time"] = formatted_time
                
                # Calculate the duration and update the information
                end_time = datetime.strptime(formatted_time, time_format) 
                start_time = self.df.loc[task_row_index, "Start time"]
                start_time = datetime.strptime(start_time, time_format)
                duration = end_time - start_time
                self.df.loc[task_row_index, "Duration"] = duration

                print(f"\n  Task {task_id} is successfully ended: ")

            else:
                print("\n  Error: This task has already be ended")
            
            # Display the task that is ended
            filtered_df = self.df[task_row_index:task_row_index+1]
            print(filtered_df.to_string(index=False, col_space=15))

        else:
            print("\n  This task ID does not exits.")
        

    def running_tasks(self):
        """
        Display all the tasks that are not ended.
        """
        running_tasks_df = self.df[self.df["End time"] == "Still running"]
        if running_tasks_df.empty:
            print("\n  There is no currently running tasks.")
        else:
            print("\n                      Currently running tasks\n")
            print(running_tasks_df.to_string(index=False, col_space=15))
    
    def show_records(self):
        """
        Display the records of all the tasks, including finished tasks and 
        currently running tasks.
        """
        
        if self.df.empty:
            print("\n  There are no task records.")
        else:
            print("\n                      All task records\n")
            print(self.df.to_string(index=False, col_space=15))

    def export_csv(self):
        """
        Export all records to CSV file. File name: task_timer_record_XXXXXXXX.csv
        The XXXXXXXX is the date and time the file was created, in the format 
        mm/dd/hh/mm, with 24-hour notation. For example, a file exported at 
        Feb 7th 6:35pm will be "task_timer_record_02071835.csv"
        """
        # Capture the current time
        current_time = datetime.now()

        # Format the current time as mmddhhmm and create file_name
        formatted_time = current_time.strftime("%m%d%H%M")
        file_name = f"task_timer_record_{formatted_time}.csv"

        # export as csv and display success message
        self.df.to_csv(file_name, index=False)  
        print("\n  Your records has been exported to a CSV file.")
        print(f"  File name: {file_name}")


    def list_commands(self):
        """"
        Display all the available commands.
        """

        commands = """
  Available command and its explanations:
  
  - start task (1)
      This will start a new task timer with a unique ID assigned by the system.
      The prompt "task name (optional):" will appear, the user can enter a task
      name or just press "ENTER" to leave it blank.
  - end task (2)
      The prompt "Please enter the task ID you want to end:" will appear, the 
      user will enter ID of task the user wish to end.
  - running tasks (3)
      This will display the tasks that are currently running.
  - show task record (4)
      All the task records will be shown, including task ID, task name, start 
      time, end time, and duration.
  - export csv (5)
      The task records will be exported as a CSV file, with the file name 
      "task_timer_record_XXXXXXXX.csv"
      The string of XXXXXXXX will be the date and time the file was created, 
      in the format mm/dd/hh/mm, with 24-hour notation. For example, a file 
      exported at Feb 7th 6:35pm will be "task_timer_record_02071835.csv"
  - help (6)
      This will display a list of commands the user can use, with explanations.
  - exit (7)
      This will exit the task timer program. A prompt will appear to ask the 
      user if they want to export the records as CSV

  Note: 
  1. The commands can be upper case or lower case. 
  2. Time format for each task is mm-dd hh:mm:ss, using the 24-hour notation. 
     For example, May 2nd 2:30:10 pm will be stored as "05-05 14:30:10"
  3. For the commands that have a number attached, the user can enter the number
     instead of typing out the whole command.
     For example, can enter "1" in place of "start task"
        """

        print(commands)