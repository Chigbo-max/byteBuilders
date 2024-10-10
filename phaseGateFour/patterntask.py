try:

	for number in range(-1,7):
		print(' ')

		for secondNumber in range(1, number):
			if (secondNumber % 2 == 0): print(end='* ')
			elif(secondNumber % 3 == 0): print(end='3 ')
			elif(secondNumber % 5 == 0): print(end='5 ')
			else: print(end='1 ')
		print(end=' ')

	for digit in range(7,1,-1):
		print(' ')

		for secondDigit in range(1,digit):
			if (secondDigit % 2 == 0): print(end='*')
			elif(secondDigit % 3 == 0): print(end='3')
			elif(secondDigit % 5 == 0): print(end='5')
			else: print(end='1')
			print(end=' ')


	choiceNumber = int(input("Enter a number: "))

	def display_fibonacci(choiceNumber):
		first_number = 0
		second_number = 0
		other_number = 1
		count = 0

		for number in range(0, choiceNumber):
			first_number = second_number
			second_number = other_number
			other_number = first_number + second_number
			count += 1
			print(other_number, end=" ")
	display_fibonacci(choiceNumber)


	input = int(input("Enter a number: "))

	def display_factorial(input):
		factorial = 1
		for numbers in range(input, 1, -1):
			factorial *= numbers
		print(factorial)

	display_factorial(input)



	def checkBooleanForLetters():
		letter = 'z'
		if (letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'): print("false, number is a consonant")
		else: print("true, number is even")
	checkBooleanForLetters()

except ValueError:
	print("Invalid input")
		
	



			

