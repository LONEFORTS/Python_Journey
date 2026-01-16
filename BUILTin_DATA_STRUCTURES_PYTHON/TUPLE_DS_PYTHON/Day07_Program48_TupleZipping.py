# Two separate tuples
names = ("Alice", "Bob", "Charlie")
scores = (85, 92, 78)

# 1. Using zip to pair them together
# This creates pairs like (Alice, 85), (Bob, 92)...
paired_data = zip(names, scores)

# 2. Convert the zipped data into a tuple of tuples
result = tuple(paired_data)

print("Paired Student Data:")
print(result)

# 3. Using zip in a loop to print nicely
print("\nIndividual Scores:")
for name, score in result:
    print(f"{name} scored {score}")
