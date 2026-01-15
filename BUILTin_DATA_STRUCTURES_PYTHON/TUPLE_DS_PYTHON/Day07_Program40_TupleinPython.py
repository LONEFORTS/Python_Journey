# Program to demonstrate Tuple in Python


#A Tuple can be defined as : Tuple is a collection of elements which is ordered and immutable
# Immutable means values of tuple cannot be changed

# Creating a tuple
student_marks = (78, 85, 67, 90, 72)

# Printing the tuple
print("Student Marks:", student_marks)

# Finding total marks using built-in function
total = sum(student_marks)
print("Total Marks:", total)

# Finding number of subjects
count = len(student_marks)
print("Number of Subjects:", count)

# Calculating percentage
percentage = total / count
print("Percentage:", percentage)

# Accessing tuple element using index
print("Marks of first subject:", student_marks[0])
