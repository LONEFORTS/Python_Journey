# --- TUPLE PACKING ---

# Packing means Assigning multiple values to a single variable
# Python automatically treats this as a tuple
student_info = "Rahul", 17, "Python", "Grade 12"

print(f"Packed Tuple: {student_info}")
print(f"Data Type: {type(student_info)}")

# --- TUPLE UNPACKING WITH STAR (*) ---

# Sometimes we don't know how many items are in the tuple
# We can use the '*' to catch the remaining items into a list
numbers = (1, 2, 3, 4, 5, 6)

first, second, *the_rest = numbers

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"The rest of the numbers (as a list): {the_rest}")

# --- NESTED TUPLE ACCESS ---

# Accessing an item inside a tuple that is inside another tuple
nested_data = ("Math", (90, 95, 88), "Science")

# To get the second score (95)
score = nested_data[1][1]
print(f"The nested score is: {score}")
