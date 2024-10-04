def divide_or_square(number: float)->int:

	number = 10

	if (number < 0): number = -number
	if type(number) not in [float, int]:
		return "Invalid input"
	if(number % 5 == 0):
		return round(number  ** 0.5, 2)
	else:
		return round(number  % 5, 2)
	
	
