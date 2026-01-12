# 1. Simple FOR loop with Input
# Asking user how many times to repeat a name
name = input("Enter your name: ")
repeat = int(input("How many times to print it? "))

print("--- Printing with For Loop ---")
for i in range(repeat):
    print(f"{i+1}. {name}")

# 2. Simple WHILE loop with Input
# Loop continues until the user types 'stop'
print("\n--- While Loop: Type 'stop' to end ---")
user_text = ""
while user_text != "stop":
    user_text = input("Enter something (or 'stop'): ")
    if user_text != "stop":
        print("You typed:", user_text)

print("Program Finished!")
