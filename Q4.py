#original list

print('Original items in a list:')
my_friends=["Jack","Smith","Paul"]
for name in my_friends:
	print(name)
print('Index of Jack befor appending is ',my_friends.index("Jack"))
#Appending

print('Items after appending in a list:')
my_friends.append("Harry")
for name in my_friends:
	print(name)
print('Index of Jack after appending is ',my_friends.index("Jack"))

#sorting
my_friends.sort()
print("After sorting:")
print(my_friends)

print(my_friends[0])
print(my_friends[1])