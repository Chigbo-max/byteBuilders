import random


def display_random_subtraction():
	count = 0
	counter = 0
	counterr = 0
	for value in range(10):
		firstRandom = random.randrange(100)
		secondRandom = random.randrange(100,200)
	
		subtraction = secondRandom - firstRandom
		
		try:
			number = int(input(f'What is {secondRandom} - {firstRandom}? '))
			count+=1
		except ValueError:
			print("invalid input: please enter an integer")
			return

		if(number == subtraction):
			print("Correct") 
			counter+=1
		else:
			print("Incorrect")
			counterr+=1
		
	print("Passed: ",counter)
	print("Failed: ",counterr)

display_random_subtraction()



