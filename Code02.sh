#!/bin/bash

# Script: Ops301d6 Challenge-02
# Author: Lamin Touray
# Purpose:Create a new bash script that performs the following:
# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.


# Prompts user for input directory path.
echo "Enter directory path"
read directory

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
echo : "Enter perferred permissions"
read permissions 

# Navigates to the directory input by the user and changes all files inside it to the input setting.

chmod -R $permissions $directory .
# Prints to the screen the directory contents and the new permissions settings of everything in the directory
ls -al

# End