# Following we are Using the PASS statement in Python
# Logic: 'pass' is a null operation. It acts as a placeholder 
# where code is syntactically required but you don't want to execute anything.

print("--- Demonstration of 'pass' Statement ---")

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n == 3:
        # We use 'pass' because Python requires a body for an 'if' statement
        # If we leave this empty, the program will crash with an IndentationError
        pass 
        print("This is a placeholder for logic we will write later for number 3.")
    else:
        print(f"Current number: {n}")

# Another common use: Empty functions or classes
def future_feature():
    pass # This function does nothing yet, but won't cause an error

print("\nLoop finished successfully using 'pass' as a placeholder.")