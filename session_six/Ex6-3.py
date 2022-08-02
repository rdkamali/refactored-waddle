# 8 -> 4 2 1
# x = 8
# i -> 7 6 5 4 3 2 1
listx =[]
x = int(input("Enter a number: "))
i = x - 1
while i > 0:
    if x % i == 0:
        listx.append(i)
    i = i - 1

# if len(listx) == 1:
#     print(x,'is a prime number')
sum1 = sum(listx)
# j = 0
# while j < len(listx):
#     sum = sum + listx[j]
#     j = j + 1
print('list->',listx)  
  
print('sum->',sum1)
if sum1 == x:
    print(x,'is a perfect number')
