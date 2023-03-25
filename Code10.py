#!/usr/bin/env python3
# Script: Ops301d6 Challenge-07
# Author: Lamin Touray
# Purpose: Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file






# Open a new file in write mode
with open('example.txt', 'w') as file:
    # Write three lines to the file
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')
    file.write('This is the third line.\n')

# Open the file in read mode
with open('example.txt', 'r') as file:
    # Read the first line of the file and print it to the screen
    first_line = file.readline()
    print(first_line)

# Delete the file
import os
os.remove('example.txt')
