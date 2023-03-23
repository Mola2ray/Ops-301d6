#!/usr/bin/env python3
# Script: Ops301d6 Challenge-08
# Author: Lamin Touray
# Purpose:  Group variables into a list, and assigns them place values to call upon one or multiple when needed.



#Main

#Establishes list and inserts values
mola = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#Outputs all values in list defined above
print(mola)

#Outputs the 4th object in list, remember 0 is the 1st object.
print(mola[3])
#Outputs the 6th through 10th value in the list
print(mola[5:10])

#Changes the 7th value in the defined list to "onion"
mola[6] = "rice"

#Outputs the defined list
print(mola)

#End