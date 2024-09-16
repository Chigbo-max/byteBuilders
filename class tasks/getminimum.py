def get_minimum(number1, number2, number3):

	smallest = number1

	
	if(number2 < number1):
		smallest = number2
	
	elif(number3 < number1):
		smallest = number3

	return smallest


print("Smallest is: ", get_minimum(6, 4, 9))
