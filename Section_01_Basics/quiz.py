salary = 8000


def printSalary():
	salary = 12000
	print("Salary:", salary)


printSalary()
print("Salary:", salary)

# Question 2
listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)

# Question
var= "James Bond"
print(var[2::-1])

# Question
sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)

# Exercise
# You are a university professor that gave a practice test to its students.
# Your job is to grade your students based on their percentage grade.
# Grading scale.
# 90–100% = A  80–89% = B  70–79% = C  60–69% = D  0–59% = F
# The percentage grade is already given as "percentage_grade" and your goal is to find the grade (A, B, C, D or F).
# For instance if your percentage_grade = 75 , your code shall return C.''

percentage_grade = 75

if percentage_grade < 60:
	print("F")
elif percentage_grade < 70:
	print("D")
elif percentage_grade < 80:
	print("C")
elif percentage_grade < 90:
	print("B")
else:
	print("A")
