#!/usr/bin/env python3
# Script: Ops301d6 Challenge-06
# Author: Lamin Touray
# Purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.


import os
def generate_directories_files(path):
    for root, directories, files in os.walk(path):
        # Print the current root directory
        print(root)
        # Print all subdirectories in the current directory
        for directory in directories:
            print(os.path.join(root, directory))
        # Print all files in the current directory
        for file in files:
            print(os.path.join(root, file))


# Ask the user for a file path
path = input("Enter the file path: ")

# Call the function to generate directories and files
generate_directories_files(path)