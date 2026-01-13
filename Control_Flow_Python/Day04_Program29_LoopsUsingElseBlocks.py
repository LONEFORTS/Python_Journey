#We are Using the 'else' block with loops
# Logic: A loop 'else' runs only if the loop was NOT interrupted by a 'break'.
# This is perfect for "Search" logic.

print("--- Professional Search Logic (Loop-Else) ---")

# A list of items in a shopping cart
cart = ["Apple", "Banana", "Milk", "Bread"]
search_item = input("Search for an item in the cart: ").capitalize()

for item in cart:
    if item == search_item:
        print(f"Success: {search_item} found in the cart!")
        break  # Exit the loop because we found it
else:
    # This runs ONLY if the loop finishes without finding the item
    print(f"Error: {search_item} is not in the cart.")

print("\nSearch operation complete.")