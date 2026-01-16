
# 1.Define two separate tuples
tuple_alpha = ("a", "b", "c")
tuple_numeric = (1, 2, 3)

print("Tuple 1:", tuple_alpha)
print("Tuple 2:", tuple_numeric)

# 2.Joining Tuples (Concatenation)
# We use the '+' operator to combine them.
# This creates a NEW tuple; it does not modify the originals.
combined_tuple = tuple_alpha + tuple_numeric

print("\nJoined Tuple (Alpha + Numeric):")
print(combined_tuple)

# 3. Multiplying Tuples (Repetition)
# We use the '*' operator to repeat the elements.
repeated_tuple = tuple_alpha * 3

print("\nRepeated Tuple (Alpha * 3):")
print(repeated_tuple)

# 4. Verifying the Originals
# Notice that tuple_alpha remains unchanged.
print("\nOriginal Alpha is still:", tuple_alpha)
