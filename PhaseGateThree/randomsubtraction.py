import random

def display_random_subtraction():
	count = 0
	counter = 0
	counterr = 0
	for value in range(10):
		firstRandom = random.randrange(100)
		secondRandom = 1 + random.randrange(100)
	
		subtraction = secondRandom - firstRandom
		
		number = int(input("Enter a number: "))
		count+=1

		if(number == subtraction):
			print("Correct") 
			counter+=1
		else:
			print("Incorrect")
			counterr+=1
		
	print("Passed: ",counter)
	print("Failed: ",counterr)

display_random_subtraction()



