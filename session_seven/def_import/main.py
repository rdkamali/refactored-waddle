from all_def import *

list_number=[]

 
print("-----------")
print("Please tell me the number of students in the class")
out = get_nember()
Get_students_numbers(out,list_number)
print(list_number)
f = average(list_number,out)
print(f"The average is {f}")
