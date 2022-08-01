x = int(input("Enter a number: "))
listx = []
i=1
while i < x:
    if x % i == 0:
        listx.append(i)
    i = i + 1
print("List ->",listx)
sum = 0
for item in listx:
    sum = sum + item
print('Sum of list ->',sum)
