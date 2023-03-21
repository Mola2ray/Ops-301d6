#!/usr/bin/env python3
# Script: Ops301d6 Challenge-06
# Author: Lamin Touray

# Requirements:
# The Python module “os” must be utilized
# At least three variables must be declared in Python that contain results of bash operations
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:

# whoami
# ip a
# lshw -short




# How to use Linux/Bash commands within Python
# First import the os library
import os

# Then use os.system to call any kind of bash command
os.system("whoami")
os.system("ip a")
os.system("lshw -short")


# Here are some Python-specific operations for you to practice
# How to print to terminal
print("Welcome to Python!")

# How to declare a variable
var_greeting = "Welcome to Python!"

# How to call a variable
print(var_greeting)
