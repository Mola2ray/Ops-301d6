#!/bin/bash

# Script: Ops301d6 Challenge-01
# Author: Lamin Touray
# Purpose:


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