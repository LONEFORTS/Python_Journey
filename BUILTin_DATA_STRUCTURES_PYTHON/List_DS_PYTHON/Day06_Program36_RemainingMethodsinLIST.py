# Program to demonstrate remaining built-in list methods in Python 3

# Creating a list
list1 = [10, 40, 20, 30, 20]

# insert(): Inserts an element at a given position used To add value at specific index
list1.insert(2, 25)
print("After insert():", list1)

# remove() Removes first occurrence of given value
# Use: To delete a specific element
list1.remove(20)
print("After remove():", list1)

# pop(): Removes and returns element from given index
# Use: To delete element using index
list1.pop(3)
print("After pop():", list1)

# reverse() Reverses the order of list elements
# Use: To reverse list
list1.reverse()
print("After reverse():", list1)

# sort():Arranges elements in ascending order
# Use: To sort list
list1.sort()
print("After sort():", list1)
