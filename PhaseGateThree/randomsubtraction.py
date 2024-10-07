import random

def display_random_subtraction():
	count = 0
	for value in range(10):
		firstRandom = 1 + random.randrange(100)
		secondRandom = 1 + random.randrange(100)
	
		subtraction = secondRandom - firstRandom
		
		number = int(input("Enter a number: "))
		count+=1

		if(number == subtraction):
			print("Correct")
		else:
			print("Incorrect")

display_random_subtraction()



