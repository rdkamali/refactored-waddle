# Function sample for session_seven
list_number=[]
# Get number from the user
def get_nember():
    number = int(input("Enter a number: "))
    return number
    
# Get all student numbers
def Get_students_numbers(n): 
    while n>0:
        print(f"Please enter student number {n}th")
        number = get_nember()
        list_number.append(number)
        n=n-1
        
# calculate the average
def average(list,n):
    s =0 
    for item in list:
        s= s +item
    # s = sum(list)
    avg = s/n
    # avg = s / len(list)
    return avg
    
        
    
              
 
print("-----------")
print("Please tell me the number of students in the class")
out = get_nember()
Get_students_numbers(out)
print(list_number)
f = average(list_number,out)
print(f"The average is {f}")
