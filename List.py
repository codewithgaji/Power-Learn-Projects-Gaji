# Empty List
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert Value at second Position
my_list[1] = 15
print(my_list)

# Extend my_list
other_list = [50, 60, 70]
my_list.extend(other_list)
print(my_list)

# Sort the list
my_list.sort()
print(my_list)

# Find and print the index of the value 30
print(my_list.index(30))