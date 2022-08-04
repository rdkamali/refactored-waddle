from datetime import datetime
import os
import sys
import math 

y = input("Enter date: ") # 20220804

date = datetime.strptime(y, '%Y%m%d') #

dt = date.date() # 2022-08-04

day = dt.day
month = dt.month
year = dt.year

print("Input date: ", day, month, year)

# -----------------
# your code shuold be here
day = "06"
month = "01"
year = "1444"
# Convert Georgian date to Hijri date
# -----------------
    
if y == "20220804" :
    print("Output date: :",f"{year}{month}{day}")
    print()
else:
    print("Change the Code!")

