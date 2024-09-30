import random

guess = int(input("Guess a number (Note that this number is the sum of two numbers): "))
		

def play_game(guess):

	first_number = random.randrange(100)
	second_number = random.randrange(100)
	
	sum_of_two_integers = first_number + second_number


	if (guess == sum_of_two_integers):
		return True
	else:
		return False

print(play_game(guess))

		