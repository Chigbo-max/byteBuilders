'''
PSEUDO CODE
1. create a function called only_floats
2. let the function take two parameters, first_number and second_number
3. let the function return 2 if both parameters are floats i.e if both are divisible by 0.01 without remainder
4. let the function return 1 if only one parameter is a float i.e if one parameter is divisible by 0.01 without remainder and the other isn't
4. let the function return 0 if neither parameter is a float i.e if none is divisible by 0.01 without a remainder
'''

def only_floats(first_number,second_number):

	if first_number < 0 or second_number < 0 :
		raise ValueError("Invalid number")

	if first_number % 0.1 == 0 and second_number % 0.1 == 0 :

		return 2

	elif (first_number % 0.1 == 0 and second_number % 0.1 != 0) or (first_number % 0.1 != 0 and second_number % 0.1 == 0):

		return 1

	else:

		return 0
	