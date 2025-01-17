percentage = int(input("Enter percentage: "))
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "D"
print("Your grade is:", grade)
