'''
PSEUDO CODE
1.create functions
2. name the function palindromic_number
3. let the function receive a parameter, store as number
4. let the function determine if the number is both a palindrome and a prime number
5. the function returns true if the number meets both conditions, otherwise false if it doesn't

BREAK DOWN
To get the prime number
1. if the number is less than or equal to one, return false as one is not a prime number
2. let there be a loop that starts counting from 2 to the number - 1 as prime numbers are numbes tht can only divide itself and one
3. if any number is divisible by the counter without a remainder, then the number is not a prime number, othrwise the number is a prime number and should return true

To determine the palindrome
1. first perform an operation that reverses a set of integers.
2. if the number is equal to the reversed number, then the number is a palindrome , otherwise its not a palindrome
3. Lastly, if the parameter is both a palindrome and a prime number, return true else return false

'''


def prime_number(number):
	if number <= 1 :
		return False
	for count in range(2,number):
		if number % count == 0:
			return False
		else:
			return True
	
def palindrome_number(number):
	reverse = 0

	while number != 0 :
		reverse = (reverse * 10) + (number % 10)
		number = number // 10
	
		if reverse == number :
			return True
		else:
			return False

def palindromic_number(number):
	if number < 0 :
		raise ValueError("Invalid number")

	if prime_number(number) and palindrome_number(number):
		return True
	else:
		return False
	
	
		