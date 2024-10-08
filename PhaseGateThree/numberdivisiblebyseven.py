number = int(input("Enter a number: "))
if(number < 0 ):
	number = -(number)

def check_number_divisible_by_seven(number):

	if(number % 7 == 0):
		return True
	else:
		return False
print(check_number_divisible_by_seven(number))


digit = int(input("Enter a number: "))

def check_number_is_a_multiple_of_three(digit):
	if (digit % 3 == 0):
		return ("hello")
	else:
		return ("bye")
print(check_number_is_a_multiple_of_three(digit))

