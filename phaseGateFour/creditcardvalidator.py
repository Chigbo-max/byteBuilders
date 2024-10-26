

		
cardNumbers = input("Hello, kindly enter card details to verify:  ")

splittedCardNumbers = list(cardNumbers);



def checkCardLength(splittedCardNumbers):
	if len(splittedCardNumbers) < 13 or len(splittedCardNumbers) > 16:
		print("Invalid number")
		print("Number must be between 13 and 16")
checkCardLength(splittedCardNumbers)


def checkPrefix(splittedCardNumbers):
		
	if (splittedCardNumbers[0] == "4"):
		print("Credit Card Type: VisaCard")
	elif(splittedCardNumbers[0] == "5"):
		print("Credit Card Type: MasterCard")
	elif(splittedCardNumbers[0] == "3" and numbers[1] == "7"):
		print("Credit Card Type: American Express Card")
	elif(splittedCardNumbers[0] == "6"):
		print("Credit Card Type: Discover Card")
	else:
		print("Credit Card Type: Invalid")
			
	return splittedCardNumbers


def displayCreditCardLength(splittedCardNumbers):

	if(len(splittedCardNumbers) >= 13 and len(splittedCardNumbers) <= 16):
			
		print("Credit Card Digit Length: ", len(splittedCardNumbers))

	return splittedCardNumbers			

def displayCreditCardNumber(splittedCardNumbers):
		
	print("Credit Card Number: ",  end=" ")

	for cardNumbers in splittedCardNumbers:
		print(cardNumbers, end =" ")
	print()

	return splittedCardNumbers			



def determineCardValidity(splittedCardNumbers):
			
	cardNumbers = [ ]

	for number in splittedCardNumbers:
		cardNumbers.append(int(number))
		
	sumOfNumbersLessThanOrEqualToFour = 0
	sumOfNumbersGreaterThanFour = 0

	for index in range(len(cardNumbers)-1, 0, -1):
		if(index % 2 == 0 and cardNumbers[index] <= 4):
			sumOfNumbersLessThanOrEqualToFour +=cardNumbers[index] * 2
			
	for index in range(len(cardNumbers)-1, 0, -1):
		if(index % 2 == 0 and cardNumbers[index] > 4 ):
			sumOfNumbersGreaterThanFour +=(cardNumbers[index] * 2) - 9

	total = sumOfNumbersLessThanOrEqualToFour + sumOfNumbersGreaterThanFour

	
	sumOfOddPositions = 0

	for index in range(len(cardNumbers) -1, 0, -1):
		if(index % 2 != 0):
			sumOfOddPositions +=cardNumbers[index]

	sumTotal = sumOfOddPositions + total

	if(sumTotal % 10 == 0):
		print("Credit Card Validity Status: Valid")		
	else:

		print("Credit Card Validity Status: Invalid")

	return cardNumbers			

checkPrefix(splittedCardNumbers)
displayCreditCardNumber(splittedCardNumbers)
displayCreditCardLength(splittedCardNumbers)
determineCardValidity(splittedCardNumbers)	

