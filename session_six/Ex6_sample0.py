# This example is for the sample code in how to use time sleep and clear screen
from os import system, name # Importing system and name from os module
from time import time, ctime ,sleep # Importing sleep from time module

print(time()) # Prints the time in seconds
print(ctime()) # Prints the time in a human readable format
print( ctime()[11:19] ) # Prints the time in a human readable format and only hour min sec
print('5 seconds later show time')
sleep(5)  # Sleeps for 5 seconds   
print( ctime()[11:19] ) # Prints the time in a human readable format and only hour min sec
print('3 seconds later clear screen and show time')
sleep(3)  # Sleeps for 3 seconds
# for windows
if name == 'nt':
    _ = system('cls') # Clears the screen
# for mac and linux
else:
    _ = system('clear') # Clears the screen
print( ctime()[11:19] ) # Prints the time in a human readable format and only hour min sec
