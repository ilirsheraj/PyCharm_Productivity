carSpeed = 70

if carSpeed > 100:
	print("You are driving too fast")
elif carSpeed < 20:
	print("You are driving too slow! This is a highway")
else:
	print("Your speed is just fine")
print("Ready")

# Exercise
# You want to hire some programmers with the following requirements:
# Master degree
# more than 2 years of experience
degree = input("Please state your university degree: Master, Bachelor or PhD? ")
experience = input("How many years of experience do you have ")

if degree == "Master" or degree == "master" or degree == "PhD" or degree == "phd":
	if int(experience) >= 2:
		print("You are accepted for the interview")
	else:
		print("You don't have enough experience")
else:
	print("You don't have the required degree")
