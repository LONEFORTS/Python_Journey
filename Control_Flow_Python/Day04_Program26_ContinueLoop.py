# Program 26: Using the CONTINUE statement in a loop
# Logic: Print numbers 1 to 10, but SKIP the number 5 and 7

print("--- Demonstration of 'continue' Statement ---")

for i in range(1, 11):
    # Check if the number is 5 or 7
    if i == 5 or i == 7:
        print(f"Skipping {i}...")
        continue  # This jumps back to the start of the loop for the next 'i'
    
    # This line will NOT execute if the 'continue' statement is triggered
    print(f"Processing number: {i}")

print("\nLoop execution finished!")