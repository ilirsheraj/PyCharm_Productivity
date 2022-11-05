# Create two inputs and take thir difference
numberA = float(input("Please enter a number: "))
numberB = float(input("Please enter another number"))
print(f"The difference between numbers A and B is {numberA - numberB}")

if numberA - numberB < 0:
	print("Negative Number")
else:
	print("Positive Number")
