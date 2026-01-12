# Program to print Fibonacci sequence up to n terms
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Logic: Each number is the sum of the two preceding ones.

n_terms = int(input("How many terms of Fibonacci do you want? "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence up to {n_terms} term:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1, end=" ")
        
        # Pythonic way to update variables (Simultaneous Assignment)
        # This replaces the need for a 'temp' variable like in C++
        nth = n1 + n2
        n1 = n2
        n2 = nth
        
        count += 1

print("\n\nSequence Generated!")
