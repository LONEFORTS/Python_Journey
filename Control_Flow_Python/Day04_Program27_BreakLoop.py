# Following Program shows the using the BREAK statement in a loop
# Logic: Search for a specific number in a range and stop the loop once found

print("--- Demonstration of 'break' Statement ---")

target = 7
print(f"Goal: Find the number {target} and stop the loop immediately.")

for i in range(1, 15):
    print(f"Checking number: {i}")
    
    if i == target:
        print(f"Target {target} found! Breaking the loop now...")
        break  # This terminates the loop completely
    
    # This line will not run once the break is triggered
    print("Moving to next...")

print("\nThe loop has been terminated.")