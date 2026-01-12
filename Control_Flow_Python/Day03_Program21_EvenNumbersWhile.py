# Program to print even numbers from 1 to 100 using a WHILE loop
# Logic: Start at 2 and increment by 2 in each step

print("--- Even Numbers from 1 to 100 ---")

# Initialize the counter at the first even number
num = 2

# The loop runs as long as num is less than or equal to 100
while num <= 100:
    print(num, end=" ")  # end="  " keeps the numbers on the same line
    
    # Increment by 2 to skip odd numbers (Logic: 2, 4, 6...)
    num = num + 2

print("\n\nLoop Finished!")
