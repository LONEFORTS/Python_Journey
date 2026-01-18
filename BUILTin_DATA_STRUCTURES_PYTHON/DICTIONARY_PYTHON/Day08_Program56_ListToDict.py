subjects = ["Maths", "Physics", "Chemistry"]
marks = [88, 76, 92]

# The zip function pairs them up
report_card = dict(zip(subjects, marks))
print(report_card)
