def divide_or_square(number: float)->int:

	NUMBER = 10

	if (NUMBER < 0): NUMBER = -number;

	if type(NUMBER) not in [float, int]:
		return "Invalid input"
	if(NUMBER % 5 == 0):
		return round(NUMBER  ** 0.5, 2)
	else:
		return round(NUMBER  % 5, 2)
	
	
