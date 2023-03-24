#!/usr/bin/env python3
# Script: Ops301d6 Challenge-09
# Author: Lamin Touray
# Purpose: 




# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b






mola = 40
tutu = 6
if mola > tutu:
  print("you are the father")
elif tutu < mola:
  print("she is my daugther") 

# Be sure to indent while writing an if statement, or else Python will error out.

mola = 40
tutu = 6
if mola <= tutu:
 print ("tutu is older than mola.") 
elif mola >= tutu:
  print("mola is older")


# Use elif to add a condition that only checks if previous condition is not met

mola = 40
tutu = 40
if mola > tutu:
  print("mola is greater than tutu")
elif mola == tutu:
  print("mola and tutu are equal")

# Use and to make two conditions

mola = 200
tutu = 33
fafa = 500
if mola > tutu and fafa > tutu:
  print("Both conditions are True")

# You can nest conditionals within each other
x = int(input("give me a value:"))
        
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
elif x < 5:
  print("x is less than 5")

# End
