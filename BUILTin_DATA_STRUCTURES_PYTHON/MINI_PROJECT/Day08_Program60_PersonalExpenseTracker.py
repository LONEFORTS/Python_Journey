# Day 05: Final Project - Personal Expense Tracker
# Logic: Using Lists of Dictionaries to manage financial data.

def main():
    # 1. SETUP
    # List to store all expense dictionaries
    expenses = [] 
    
    # Tuple for fixed categories (Locked choices)
    VALID_CATEGORIES = ("Food", "Transport", "Entertainment", "Bills", "Other")
    
    # Dictionary for summary totals
    summary = {"Total": 0.0}

    print("--- 💰 Personal Expense Tracker v1.0 💰 ---")
    print(f"Supported Categories: {VALID_CATEGORIES}")

    while True:
        print("\n--- MENU ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Reset All Data")
        print("5. Exit")
        
        choice = input("\nAction: ")

        if choice == "1":
            # Taking Input
            item = input("What did you buy? ").capitalize()
            amount = float(input("How much did it cost? "))
            
            print(f"Select Category: {VALID_CATEGORIES}")
            cat = input("Enter category name: ").capitalize()

            if cat not in VALID_CATEGORIES:
                print("Invalid category! Defaulting to 'Other'.")
                cat = "Other"

            # Create a Dictionary for this specific expense
            entry = {
                "item": item,
                "amount": amount,
                "category": cat
            }
            
            # Add the dictionary to our main list
            expenses.append(entry)
            summary["Total"] += amount
            print(f"Successfully added: {item}")

        elif choice == "2":
            print("\n--- Expense Log ---")
            if not expenses:
                print("No expenses recorded yet.")
            else:
                for i, exp in enumerate(expenses, 1):
                    # Accessing dictionary values inside the list
                    print(f"{i}. {exp['item']} | ${exp['amount']} | [{exp['category']}]")
                print(f"-------------------\nTOTAL SPENT: ${summary['Total']}")

        elif choice == "3":
            # Logic: Filter the list based on category
            search_cat = input("Which category summary? ").capitalize()
            cat_total = 0
            count = 0
            
            for exp in expenses:
                if exp['category'] == search_cat:
                    cat_total += exp['amount']
                    count += 1
            
            print(f"\nCategory: {search_cat}")
            print(f"Items found: {count}")
            print(f"Total spent in this category: ${cat_total}")

        elif choice == "4":
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == 'yes':
                expenses.clear()
                summary["Total"] = 0
                print("All data wiped.")

        elif choice == "5":
            print("Exporting data... Goodbye!")
            break
        
        else:
            print("Invalid choice! Try 1-5.")

if __name__ == "__main__":
    main()
