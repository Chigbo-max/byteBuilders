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
		if(choiceNumber > 0):
			first_number = 0
			second_number = 1
			#other_number = 0			

			for number in range(-1, choiceNumber):
				print(first_number, end=" ")

				other_number = first_number + second_number

				first_number = second_number
				second_number = other_number
		else:
			print("Invalid number, enter a number from 1")
	display_fibonacci(choiceNumber)


	digit = int(input("Enter a number: "))

	def display_factorial(digit):
		if (digit > 0):
			factorial = 1
			for numbers in range(digit, 1, -1):
				factorial *= numbers
			print(factorial)
		else:
			print("invalid number, enter a number from 1")

	display_factorial(digit)


	letter = input("enter a character: ")
	def checkBooleanForLetters(letter):
		if (letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'): print("false")
		else: print("true, letter is a vowel")
	checkBooleanForLetters(letter)

except ValueError:
	print("Invalid input")
		
	



			

