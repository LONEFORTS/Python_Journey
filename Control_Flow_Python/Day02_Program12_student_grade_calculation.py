# This Program is to calculate grade from marks of 5 subjects

Subject1 = int(input("Enter marks of Subject 1: "))
Subject2= int(input("Enter marks of Subject 2: "))
Subject3= int(input("Enter marks of Subject 3: "))
Subject4 = int(input("Enter marks of Subject 4: "))
Subject5 = int(input("Enter marks of Subject 5: "))

total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
print("Grade: A")
elif percentage >= 75:
print("Grade: B")
elif percentage >= 60:
print("Grade: C")
elif percentage >= 40:
print("Grade: D")
else:
print("Grade: Fail")