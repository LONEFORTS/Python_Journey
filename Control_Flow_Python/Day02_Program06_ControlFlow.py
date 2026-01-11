 
# This program demonstrates the use of multiple independent 'if' statements.
It checks whether a student is eligible for a certificate based on:
1. Passing marks
2. Attendance percentage
3. Assignment submission 

# Input values

marks = int(input("Enter student marks (0-100): "))
attendance = int(input("Enter attendance percentage: "))
assignment_submitted = input("Assignment submitted (yes/no): ").lower()

# Check if student has passed
if marks >= 40:
    print("Student has passed the examination.")

# Check attendance eligibility
if attendance >= 75:
    print("Attendance requirement satisfied.")

# Check assignment submission
if assignment_submitted == "yes":
    print("Assignment submission confirmed.")

# Final:
print("Eligibility checks completed.")