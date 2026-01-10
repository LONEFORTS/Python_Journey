print("--- MSBTE Student Enrollment System ---")

# 1. Taking Inputs From the User
name = input("Enter your Full Name: ")
enrollment_no = input("Enter your Enrollment Number: ")
branch = input("Enter your Branch (Example: CO/IF): ")
sem_percentage = float(input("Enter your last Semester Percentage: "))

# 2. Displaying Outputs (Data Presentation)
print("="*30) #"="*30 it shows the =============== the lines for good-looking
print("STUDENT PROFILE CREATED")
print("="*30)
print(f"Name         : {name}")
print(f"Enrollment   : {enrollment_no}")
print(f"Department   : {branch}")
print(f"Performance  : {sem_percentage}%")
print("="*30) #"="*30 it shows the =============== the lines for good-looking
