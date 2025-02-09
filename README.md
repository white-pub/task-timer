# Task Timer

## Description
This python program is built to track time and will display the record to the user.

This program used uv for project and virtual environment management.

## Usage
To use this program, make sure that the source code, dependencies, and uv are installed, then run the following code in the terminal "uv run python -m task_timer"

Available command and its explanations:

- start task (1)  
    This will start a new task timer with a unique ID assigned by the system.  
    The prompt "task name (optional):" will appear, the user can enter a task name or just press "ENTER" to leave it blank.
- end task (2)  
    The prompt "Please enter the task ID you want to end:" will appear, the user will enter ID of task the user wish to end.
- running tasks (3)  
    This will display the tasks that are currently running.
- show task record (4)  
    All the task records will be shown, including task ID, task name, start time, end time, and duration.
- export csv (5)  
    The task records will be exported as a CSV file, with the file name "task_timer_record_XXXXXXXX.csv"  
    The string of XXXXXXXX will be the date and time the file was created, in the format mm/dd/hh/mm, with 24-hour notation.  
    For example, a file exported at Feb 7th 6:35pm will be "task_timer_record_02071835.csv"
- help (6)  
    This will display a list of commands the user can use, with explanations.
- exit (7)  
    This will exit the task timer program. A prompt will appear to ask the user if they want to export the records as CSV

Note: 
1. The commands can be upper case or lower case. 
2. Time format for each task is mm-dd hh:mm:ss, using the 24-hour notation.  
    For example, May 2nd 2:30:10 pm will be stored as "05-05 14:30:10"
3. For the commands that have a number attached, the user can enter the number instead of typing out the whole command.  
    For example, can enter "1" in place of "start task"
