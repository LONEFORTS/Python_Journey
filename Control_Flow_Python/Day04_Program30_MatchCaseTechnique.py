# Structural Pattern Matching (Match-Case)
# Introduced in Python 3.10 - This is the modern replacement for long if-elif chains.

def check_status(status_code):
    match status_code:
        case 200:
            return "Success: Everything is working!"
        case 404:
            return "Error: Page not found!"
        case 500:
            return "Error: Server is down!"
        case 401 | 403: # The | means "OR"
            return "Authentication Error: Access Denied!"
        case _: # The underscore is the 'default' case (like 'else')
            return "Unknown Status: Something went wrong."

# Testing the modern logic
code = int(input("Enter a website status code (e.g., 200, 404, 500): "))
result = check_status(code)
print(result)

# Why this is better:
# 1. It is more readable than 10 'if-elif' statements.
# 2. It allows matching multiple patterns (using |).
# 3. It is the standard for modern Python 3.10+ development.