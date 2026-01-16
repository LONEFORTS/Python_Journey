#whenever there is . it is a method according to me

# Create a tuple with some repeated numbers
my_data = (10, 20, 30, 20, 40, 20, 5, 100)
print(f"My Tuple: {my_data}")

# Count how many times '20' appears
print(f"Count of 20: {my_data.count(20)}")

# Find the position (index) of the number 30
print(f"Index of 30: {my_data.index(30)}")

# Check how many items are in the tuple
print(f"Length of tuple: {len(my_data)}")

# Find the biggest and smallest numbers
print(f"Largest number: {max(my_data)}")
print(f"Smallest number: {min(my_data)}")

# Add all numbers together
print(f"Total sum: {sum(my_data)}")

# Sort the numbers (this creates a list)
print(f"Sorted version: {sorted(my_data)}")

# Join two tuples together
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print(f"Joined tuples: {combined}")

# Repeat a tuple
repeated = tuple1 * 3
print(f"Repeated tuple: {repeated}")

# Check if a number exists in the tuple (True or False)
print(f"Is 50 in there? {50 in my_data}")
