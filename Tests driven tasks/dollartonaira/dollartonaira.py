"""
PSEUDO CODE
1. create a function
2. name the function dollar_to_naira
3. prompt user to enter amount in dollar
4. let exchange rate of one dollar to naira be 1550 naira
5. multiply amount entered in dollar by 1550 naira
6. display result

"""
amount = 1
def dollar_to_naira(amount):

	dollar_amount = float(input("Enter amount in dollar: "))

	if (amount <= 0):

		raise ValueError("Invalid number")

	DOLLAR_EXCHANGE_RATE = 1550

	dollar_to_naira = DOLLAR_EXCHANGE_RATE * dollar_amount

	return dollar_to_naira

