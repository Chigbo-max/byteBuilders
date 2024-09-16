'''
PSEUDO CODE
1. create a function named divide_or_square
2. let the function have a paremeter named input
3. the function returns the square root if the number is divisible by 5
4. if the number is not divisible by 5, the function returns the remainder of the number divided by five
if number is negative, handle it
if input is non-integer, handle it
'''

def divide_or_square(number):
	if number < 0 :
		raise ValueError("Invalid number")

	if number % 5 == 0 :
		return number ** 0.5
	else:
		return number % 5
	
	