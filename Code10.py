#!/usr/bin/env python3
# Script: Ops301d6 Challenge-09
# Author: Lamin Touray
# Purpose: Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file

# newfile = open("test.txt", "w")

# # How to open a file
# openfile = open("test.txt")

# # How to return the five first characters of a file
# read = open("test.txt", "r")
# print("test.txt"(readline(1))




# Open a new file in write mode
with open("example.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Open the file in read mode
with open("example.txt", "r") as file:
    for i in range(3):
     first_line = file.readline()
    print(first_line)

# Delete the file
import os
os.remove("example.txt")
