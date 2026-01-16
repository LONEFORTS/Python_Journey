#Follwing is the program on tuple immutability, here tuple immutability means internal state or elements cannot be changed, added, or removed.
# 1. Define a tuple
# Once created, the elements inside 'coordinates' are locked.
coordinates = (10, 20, 30)
print("Original Tuple:", coordinates)

# 2. Attempting to modify an element
# In a List, we could do coordinates[0] = 99. 
# In a Tuple, this will raise a TypeError.

print("\n--- Attempting to change index 0 to 99 ---")

try:
    # This line will trigger an exception
    coordinates[0] = 99
except TypeError as e:
    # We catch the error so the program doesn't just crash
    print(f"PYTHON ERROR: {e}")
    print("REASON: Tuples do not support 'item assignment'.")

# 3. Showing what IS allowed
# While you can't change the tuple, you can reassign the variable 
# name to a brand new tuple.
coordinates = (40, 50, 60)
print("\nNew Tuple (Reassigned):", coordinates)
print("Note: We didn't change the old tuple; we created a whole new one.")
