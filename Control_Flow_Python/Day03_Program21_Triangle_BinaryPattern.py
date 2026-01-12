# Program to print a decreasing binary pattern (1010101, 10101, etc.)
# Logic: Outer loop handles the number of characters (7, 5, 3, 1)
# Inner loop handles the alternating 1s and 0s

print("--- Binary Pattern ---")

# We start with 7 characters and go down to 1
# range(start, stop, step) -> range(7, 0, -2)
for i in range(7, 0, -2):
    
    # Inner loop runs 'i' times for the current row
    for j in range(i):
        # Logic: If index is even, print 1. If odd, print 0.
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
            
    # Move to the next line after the inner loop finishes
    print()

print("\nPattern Complete!")
