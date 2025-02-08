# Task Timer
Anna Chen
Jan 2025

## Description
This python program is built to track time and will display the record to the user.

This program used uv for project and virtual environment management.

For now, there is only a simple "Hello" function.

## Usage
To use this program, make sure that the source code, dependencies, and uv are installed, then run the following code in the terminal "uv run task-timer"

Available command and explinations:
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
    The task records will be exported as a csv file, with the file name task_timer_record_XXXXXXXX.csv
    The string of XXXXXXXX will be the date and time the file was created, in the format mm/dd/hh/mm, with 24-hour notation.
    For example, a file exported at Feb 7th 6:35pm will be "task_timer_record_02071835.csv"
- help
    This will display a list of commands the user can use, with explanations.
- exit
    This will exit the task timer program. A prompt will appear to ask the user if they want to export the records as csv

Note: The commands can be upper case or lower case.






