# Create a tuple of daily tasks
tasks = ("Code", "Exercise", "Read", "Sleep")

# 1. Simple 'for' loop to print each item
print("My Daily Tasks:")
for task in tasks:
    print(f"- {task}")

# 2. Checking if an item exists (Membership)
# This uses the 'in' keyword
goal = "Code"
if goal in tasks:
    print(f"\nYes, {goal} is in my task list!")

# 3. Looping with index numbers
# This uses range() and len() to show positions
print("\nTasks with their positions:")
for i in range(len(tasks)):
    print(f"Task {i+1}: {tasks[i]}")
