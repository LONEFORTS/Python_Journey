# Topic: Tuple Unpacking
# Assigning values from a tuple to multiple variables in one line.

# 1. Defining a basic tuple (representing a fruit's data)
# Format: (Name, Color, Calories)
fruit_data = ("Apple", "Red", 95)

# 2. Basic Unpacking
# Instead of doing name = fruit_data[0], we do this:
name, color, calories = fruit_data

print("--- Basic Unpacking ---")
print("Fruit Name:", name)
print("Color:", color)
print("Calories:", calories)

# 3. Unpacking with specific variables
# Note: The number of variables must match the number of items in the tuple.
point = (10, 20, 30)
x, y, z = point

print("\n--- Coordinate Unpacking ---")
print(f"X: {x}, Y: {y}, Z: {z}")

# 4. Use Case: Swapping two variables using tuples
# This is a classic Python trick!
a = "First"
b = "Last"

print("\n--- Swapping Variables ---")
print("Before swap:", a, b)

# Python creates a temporary tuple and unpacks it back
a, b = b, a 

print("After swap:", a, b)
