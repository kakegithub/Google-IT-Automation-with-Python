#!/usr/bin/env python3

# Windows file directory
# C:\my-directory\target-file.txt

# Windows file directory written in Python
# C:/my-directory/target-file.txt.

# #Windows file directory
# C:\\my-directory\\target-file.txt

# #CWD command:
# os.getcwd()

# #CWD command for external files:
# outputs['current_directory_before'] = os.getcwd()

import os
import datetime

os.path.exists("novel.txt")  # Check if the file exists
os.path.exists("declaration.txt")  # Check if the file exists


print("-------------------------------------------------------")

# Get the current working directory
# os.remove("novel.txt")  # Remove the file if it exoists


print("--------------------------------------------------------")

# Get the current working directory
# os.remove("novel.txt")
# os.remove("novel.txt")
print("---------------------------------------------------------")


# os.rename("novel.txt", "novel.txt.bak")  # Rename the file if it exists
# os.rename("novel.txt.bak", "novel.txt")  # Rename it back to original name

print("---------------------------------------------------------")

tam = os.path.getsize("spider.txt")  # Get the size of the file in bytes
print(tam)  # Print the size of the file in bytes

mod = os.path.getmtime("spider.txt")  # Get the last modified time of the file
print(mod)  # Print the last modified time in seconds since epoch


print("---------------------------------------------------------")

timestamp = os.path.getmtime("spider.txt")  # Get the last modified time of the file
datetime.datetime.fromtimestamp(timestamp)
# Convert the timestamp to a human-readable format
print(datetime.datetime.fromtimestamp(timestamp))  # Print the last modified time
print("---------------------------------------------------------")


ruta = os.path.abspath("spider.txt")
# This code takes the file name and turns it into an absolute path
print(ruta)  # Print the absolute path of the file
