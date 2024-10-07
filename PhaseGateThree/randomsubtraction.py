import random

number = int(input("Enter a number: "))
count = 0
def display_random_subtraction(number):
	for value in range(10):
		firstRandom = 1 + random.randrange(100)
		secondRandom = 1 + random.randrange(100)
	
		subtraction = secondRandom - firstRandom

		if(number == subtraction):
			print("Correct")
		else:
			print("Incorrect")
		
		count+=1
print(display_random_subtraction(number))



