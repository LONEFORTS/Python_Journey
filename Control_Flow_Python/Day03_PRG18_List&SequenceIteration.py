#This program demonstrates how Python loops iterate through sequences
#Python handles the index (i) automatically behind the scenes

# Example 1: Iterating through a String
# The variable 'letter' automatically receives one character at a time
print("--- String Iteration ---")
for letter in "Python":
    print("Current Letter:", letter)

# Example 2: Iterating through a List
# The variable 'fruit' automatically receives one item at a time from the list
print("\n--- List Iteration ---")
fruits = ['Apple', 'Strawberry', 'Mango'] 
for fruit in fruits:
    # 'fruit' is the individual item, 'fruits' is the whole collection
    print("Current Fruit:", fruit)

print("\nGood Bye!")
