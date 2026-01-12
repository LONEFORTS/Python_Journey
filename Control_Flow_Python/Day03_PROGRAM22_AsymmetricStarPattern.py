# Program to print a specific asymmetric star pattern
# Pattern logic: 1, 3, 4, 3, 1 stars per row

print("--- Asymmetric Star Pattern ---")

# We can use a list to define the number of stars per row
# This demonstrates the 'Sequence Iteration' we learned earlier today!
star_counts = [1, 3, 4, 3, 1]

for count in star_counts:
    # Logic: If it's a single star, we add a space to center it
    if count == 1:
        print(" * ")
    else:
        # Python 'String Multiplication' trick: "*" * 3 results in "***"
        print("*" * count)

print("\nGood Bye!")
