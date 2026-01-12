# following is the program of Nested Loop in python its : A loop inside another loop (useful for grids/matrices)

print("--- Grid Sector Scan ---")

# Outer loop for rows
for row in range(1, 4):
    # Inner loop for columns
    for col in range(1, 3):
        print(f"[Row {row}, Col {col}]", end=" ")
    print() # New line after each row

print("Scan Complete.")
