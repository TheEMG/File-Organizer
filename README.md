# Windows File Organizer 
This Python Script is designed to automatically organize files in your desired directory(the Downloads folder was used in this script but can be modified) by catergorizing them based on their file extension. It moves 
each file into corresponding subfolders (e.g., .txt, .jpg, .pdf, etc.) inside a specified target directory.

## How it works 
- Script scans the source folder (In this example the downloads folder).
- It then catergorizes the files based on their extensions and moves them into folder named after the extension.
- Files without the extensions are moved to a folder named other.
- If the target directory or the neccesary extension folders do not exist, the script will create them automatically.

## Warning : Backup your files 
Before using this script, ensure that you back up important files. This script will move files from your source folder (Downloads) to the target folder. Once the files are moved, they will no longer exist in the original location, which could cause data loss if you are not prepared.

## Usage 
- Task Scheduler:
  - This script is intended to work with Windows Task Scheduler. It is recommended to scheduler this taks daily or at any desired frequency.
  - Example setup using Task Scheduler:
      - Create a new task
      - Set the trigger to run daily (or at another interval)
      - Set the action to run your Python Script
      - Set the action to run your Python Script
      - Refer to  [How to Schedule a Python Script with Windows Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page).
   

## What I have learn 
- File sorting efficiency: The script can handle large direcotries efficiently, but it's important to choose the right organizational structure for your use case.
- Python OS Module: Using os and shutil libraries makes file manipulation straightforward in Python.
- Automation: Scheduling Python scripts with Task Scheduler simplifies repeated tasks without requiring manual intervention.
