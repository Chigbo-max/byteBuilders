
def display_multiplication(firstNumber,secondNumber: float)->int:

	if type(firstNumber) not in [int, float]:
		return "Invalid input"

	if (secondNumber < 0 and firstNumber > 0):
		temp = secondNumber;
		secondNumber = firstNumber;
		firstNumber = temp;
	if (secondNumber < 0 and firstNumber < 0):
		secondNumber = -secondNumber
		firstNumber = -firstNumber
	multiplication = 0
	
	for number in range(1, 3):
		multiplication += 3.2
	return multiplication

	
