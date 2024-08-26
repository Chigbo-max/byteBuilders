score = int(input("Enter score: "))

if score > 100:
	print("invalid number")

elif score >= 75 and score <= 100:
	print("Your grade is A")
elif score >= 65 and score <= 74:
	print("Your grade is B")
elif score >= 50 and score <= 64:
	print("Your grade is C")
elif score >= 40 and score <= 49:
	print("Your grade is D")
else:
	print("failed")