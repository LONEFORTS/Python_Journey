

# This program demonstrates the use of a nested if statement.


# Input from the user
num = int(input("Enter an integer number: "))

# Outer if condition
if num > 0:
    print("The number is POSITIVE.")

    # Inner if condition
    if num % 2 == 0:
        print("The number is EVEN.")
    else:
        print("The number is ODD.")


print("Program execution completed.")