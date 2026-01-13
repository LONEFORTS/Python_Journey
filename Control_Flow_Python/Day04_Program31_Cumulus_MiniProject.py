# Mini Project: Cumulus Calculator
# Description: This project demonstrates the practical use of variables,
# operators, conditional statements, and loops I learned from 20+ programs.



print("--- Welcome to the Day 04 Calculator & Logger ---")

# We will keep a list to store our calculation history
history = []

while True:
    print("\n[Choices: +, -, *, /, history, exit]")
    operation = input("What do you want to do? ").lower()

    # 1. Handle the Exit first
    if operation == "exit":
        print("Closing the program. Great job on Day 04!")
        break

    # 2. Handle the History display (Using a For Loop)
    if operation == "history":
        print("\n--- Your Recent Calculations ---")
        if not history:
            print("No history found yet.")
        else:
            for record in history:
                print(f"Result: {record}")
        continue # Go back to the start of the loop

    # 3. Perform Calculations (If-Else Logic)
    if operation in ["+", "-", "*", "/"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error (Divide by zero)"
            else:
                result = num1 / num2

        print(f"The answer is: {result}")
        
        # Add the result to our history list
        history.append(f"{num1} {operation} {num2} = {result}")

    else:
        print("Invalid Choice! Please pick a math sign or type 'exit'.")

print("\n--- Project Finished ---")