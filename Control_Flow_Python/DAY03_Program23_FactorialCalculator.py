# Program to calculate the Factorial of a number
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Input from the user
num = int(input("Enter a number to find its factorial: "))

# Initialize factorial variable to 1
# (Note: Factorial of 0 is 1, and we use 1 as a starting point for multiplication)
factorial = 1

# Logic check for the input number
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Loop from 1 to num (inclusive)
    for i in range(1, num + 1):
        factorial = factorial * i
    
    print(f"The factorial of {num} is {factorial}")

# Fact: In Python, you can calculate the factorial of huge numbers 
# like 100 without any memory overflow errors!
