# You can run each part separately or comment on the others
print('-------part 0-------')
x = [] 
print(type(x))

x = [1, 2, 3, 4, 5]
print(x)
print(x[0])
print(x[1])

x = [1, 1.3, 'a', 4, 5]
print(x)
print(x[1])
print(x[2])
print(x[-5])
print(x[-1])
print(x[5])

print('-------part 1-------')
friends = ['John','Michael','Terry','Eric','Graham']
print(friends) # ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends[1]) # Michael
print(friends[1],friends[4]) # ›Michael Graham
print(len(friends)) # 5
print(friends.count('Eric')) # 1

print('-------part 2-------')
friends = ['John','Michael','Terry','Eric','Graham']
friends.append('TerryG') # add TerryG to the end of the list
print(friends) # ['John', 'Michael', 'Terry', 'Eric', 'Graham', 'TerryG']

print('-------part 3-------')
friends = ['John','Michael','Terry','Eric','Graham']
friends[2]='TerryG' # change the value of Terry to TerryG
print(friends) # ['John', 'Michael', 'TerryG', 'Eric', 'Graham']

print('-------part 4-------')
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.extend(cars) # add cars to the end of the list
print(friends) # ['John', 'Michael', 'TerryG', 'Eric', 'Graham', 911, 130, 328, 535, 740, 308]

print('-------part 5-------')
friends = ['John','Michael','Terry','Eric','Graham']
friends.remove('Terry') # remove Terry from the list
print(friends) # ['John', 'Michael', 'Eric', 'Graham']


print('-------part 6-------')

friends = ['John','Michael','Terry','Eric','Graham']
friends.pop(2) # remove the element at index 2
print(friends) # ['John', 'Michael', 'Eric', 'Graham']
friends.pop(-1) # remove the last element
print(friends) # ['John', 'Michael', 'Eric']


print('-------part 7-------')
friends = ['John','Michael','Terry','Eric','Graham']
del friends[2] # remove the element at index 2
print(friends) # ['John', 'Michael', 'Eric']

print(friends)
friends = ['John','Michael','Terry','Eric','Graham']
del friends # delete the list
print(friends) # NameError: name 'friends' is not defined


print('-------part 8-------')

for letter in 'Norwegian blue':
    print(letter)
print("For Loop done!")

print('-------part 9-------')
for name in ['John','Terry','Eric','Michael','George']:
    print(name)

print("For Loop done!")

print('-------part 10-------')
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    print(friend)

print("For Loop done!")

print('-------part 11-------')
friends = ['John','Terry','Eric','Michael','George']
for index in range(len(friends)):
   print(friends[index])

print("For Loop done!")

print('-------part 12-------')
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        break # exit the loop
    print(friend)

print("For Loop done!")

print('-------part 12-------')
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        continue # skip this iteration
    print(friend)

print("For Loop done!")
