#!/bin/bash
#Ops301d6: Code Challenge-01
#Author: Lamin Touray
#Purpose: Create a bash script that:

#Copies /var/log/syslog to the current working directory
#Appends the current date and time to the filename

cp /var/log/syslog ./




# Define the filename
filename="syslog"

# Get the current date and time in the format yyyy-mm-dd-HH-MM-SS
datetime=$(date +%Y-%m-%d-%H-%M-%S)

# Append the date and time to the filename
new_filename="${filename}_${datetime}"

# Rename the file
cp "$filename" "$new_filename"
rm "syslog"






