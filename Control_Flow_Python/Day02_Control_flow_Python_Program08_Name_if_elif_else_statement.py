 
# This program demonstrates the use of if-elif-else statement
to check whether a given number is:
1. Positive
2. Negative
3. Zero


# Accept input from the user
num = int(input("Enter an integer number: "))

# Decision making using if-elif-else
if num > 0:
    print("The number is POSITIVE.")
elif num < 0:
    print("The number is NEGATIVE.")
else:
    print("The number is ZERO.")

# Program end message
print("Program execution completed.")