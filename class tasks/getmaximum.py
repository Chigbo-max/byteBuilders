number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

def get_maximum(number1, number2, number3):

	largest = number1

	
	if(number2 > number1):
		largest = number2
	
	elif(number3 > number1):
		largest = number3

	return largest


print("Largest is: ", get_maximum(number1, number2, number3))


def get_minimum(number1, number2, number3):

	smallest = number1

	
	if(number2 < number1):
		smallest = number2
	
	elif(number3 < number1):
		smallest = number3

	return smallest


print("Smallest is: ", get_minimum(number1, number2, number3))
