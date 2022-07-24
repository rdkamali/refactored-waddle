from os import system, name # Importing system and name from os module
from time import sleep # Importing sleep from time module

print("Welcome to the help machine")
while True: # Infinite loop
    # for windows
    if name == 'nt':
        _ = system('cls') # Clears the screen
   # for mac and linux
    else:
        _ = system('clear') # Clears the screen
    print("-------------------------------------")  
    print("List of commands:")
    print("Type 'avarage' to get the average of the numbers")
    print("Type 'quit' to exit")
    menu = input("Chose an option: ")
    if menu == "avarage":
        print("Type the numbers you want to average")
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        print("The average of the numbers is: " + str((num1 + num2) / 2))
        sleep(5) # Sleeps for 5 seconds
    elif menu == "quit":
        break #
    else:
        print("Invalid command")
        sleep(3) # Sleeps for 3 seconds
    
print("-------------------------------------")    
print("Thank you for using the help machine")
