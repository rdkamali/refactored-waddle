# You can run each part separately or comment on the others
print('-------part 0-------')
a = 1
b  = a < 5
print(type(b))
print(b)
b  = a > 5
print(type(b))
print(b)
if b:
    print('b is true')
else:
    print('b is false')
    
if 1<5 and 2<3:
    print('true')
else:
    print('false')
    
print('-------part 1-------')
x = input("Please enter a char: ")
if x == 'a':
    print('a')
elif x == 'b':
    print('b')
elif x == 'c':
    print('c')
elif x == 'd':
    print('d')
elif x == 'e':
    print('e')
else: 
    print('other')
print('-------part 3-------')
while True:
    print('hello')
print('bye')
print('-------part 4-------')
x = 1>5
while x:
    print('hello')
print('bye')

print('-------part 5-------')
i = 0
sum = 0
while i < 10:
    x = input("Enter a number: ")
    sum = int(x) + sum
    
print('sum is: ', sum)

print('-------part 6-------')
i = 0
sum = 0
while i < 10:
    x = input("Enter a number: ")
    sum = int(x) + sum
    i = i + 1
    print("The sum is: ", sum)
    print("The number is: ", i)
    
average = sum / 10
print("The average is: ", average)
print('-------part 7-------')
i = 0
while i < 10:
    
    i = i + 1
    if i % 5 == 0:
        print("HOPE")
    else:
        print(i)
print('-------part 8-------')

a=1
b=1
n=20
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
