# follwing is Program to demonstrate built-in list methods in Python 3

# Creating two lists
list1 = [10, 20, 30, 20]
list2 = [40, 50]

# append(): Adds one element at the end of the list
# Use: To insert a single new value
list1.append(60)
print("After append():", list1)

# clear(): Removes all elements from the list
# Use: To make list empty
list2.clear()
print("After clear():", list2)

# Reassigning values to list2
list2 = [40, 50]

# copy(): Creates a duplicate copy of the list
# Use: To copy list without changing original
list3 = list1.copy()
print("After copy():", list3)

# count(): Counts number of occurrences of an element
# Use: To find frequency of element
print("Count of 20:", list1.count(20))

# extend(): Adds elements of another list
# Use: To combine two lists
list1.extend(list2)
print("After extend():", list1)

# index(): Returns index of first occurrence
# Use: To find position of element
print("Index of 30:", list1.index(30)) 



#There are some more remaining methods built in of python will be shown in Program36