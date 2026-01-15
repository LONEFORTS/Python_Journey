#Following is simple Student Result Management System.

# Creating empty list to store marks
marks = []

# Taking student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")

# Taking marks of 5 subjects
for i in range(1, 6):
    m = int(input("Enter marks of subject " + str(i) + ": "))
    marks.append(m)

# Calculating total and percentage
total = sum(marks)
percentage = total / len(marks)

# Finding pass or fail
fail_count = 0

for m in marks:
    if m < 35:
        fail_count = fail_count + 1

# Result and grade decision
if fail_count > 0:
    result = "FAIL"
    grade = "No Grade"
else:
    result = "PASS"
    if percentage >= 75:
        grade = "Distinction"
    elif percentage >= 60:
        grade = "First Class"
    elif percentage >= 50:
        grade = "Second Class"
    else:
        grade = "Pass Class"

# Displaying result
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll No:", roll)
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", result)
print("Grade:", grade)
