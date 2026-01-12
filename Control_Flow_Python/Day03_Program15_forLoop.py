# Following program is of for loop in python its Goal is to Iterate over a sequence (range of numbers)

print("--- Inventory List ---")
items = ["Scanner", "Processor", "Sensor", "Relay"]

# Iterating through a list using for loop
for i in range(len(items)):
    print(f"Item {i+1}: {items[i]}")

print("Inventory Check Complete.")
