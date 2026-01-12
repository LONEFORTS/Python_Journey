# Program to check if a number is a Palindrome
# A palindrome number reads the same backward as forward (e.g., 121)

# Taking input from the user
num = int(input("Enter a number to check: "))

# We store the original number to compare it later
temp = num
reverse_num = 0

# Logic to reverse the number
while temp > 0:
    # Get the last digit (e.g., 121 % 10 = 1)
    remainder = temp % 10
    
    # Build the reversed number (Shifting digits to the left)
    reverse_num = (reverse_num * 10) + remainder
    
    # Remove the last digit from temp (Integer division)
    temp = temp // 10

# Final check: compare original with reversed
if num == reverse_num:
    print(f"Yes, {num} is a Palindrome!")
else:
    print(f"No, {num} is not a Palindrome.")
