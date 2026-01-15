# Program to find common elements in two lists

# Creating two lists
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

# Finding common elements here's the logic the i goes to List1 elements check each for #example here's if condition for I when I get 30 at list1 it directly checks the if #condition here.
common_list = []

for i in list1:
    if i in list2:
        common_list.append(i)

# Displaying common elements
print("Common elements:", common_list)
