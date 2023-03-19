#!/bin/bash
# Script: Ops301d6 Challenge-04
# Author: Lamin Touray
# Write a bash script that performs the following tasks:

# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip


# Define the log files to be backed up
log_files="/var/log/syslog /var/log/wtmp"

# Define the backup directory
backup_dir="/var/log/backups"

# Get the current timestamp
timestamp=$(date +%Y%m%d%H%M%S)

# Loop through each log file and perform the backup
for file in $log_files
do
  # Get the original file size
  original_size=$(du -h "$file" | cut -f1)

  # Compress the file and save it to the backup directory with a timestamp
  backup_file="${backup_dir}/$(basename $file)-${timestamp}.zip"
  zip -q "$backup_file" "$file"

  # Clear the contents of the log file
  echo "" > "$file"

  # Get the compressed file size
  compressed_size=$(du -h "$backup_file" | cut -f1)

  # Print the file sizes to the screen
  echo "Original file size: ${original_size}"
  echo "Compressed file size: ${compressed_size}"

  # Compare the file sizes
  if [[ $(echo "${original_size} < ${compressed_size}" | bc -l) -eq 1 ]]; then
    echo "The compressed file is smaller than the original file"
  else
    echo "The compressed file is larger than the original file"
  fi
done

# Source: chatGPT