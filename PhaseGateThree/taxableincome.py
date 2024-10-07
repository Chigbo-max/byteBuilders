print(
'''
0 single fliers
1 married filling jointly
2 married filling separately

''')

userInput = int(input("Enter number: "))

if (userInput == 0):
	amount = 0
	balance = 0
	deduction = 0
	taxable_income = float(input("Enter income: "))
	if (taxable_income < 0): raise ValueError("invalid input")
	if (taxable_income >= 0 and taxable_income <= 8350):
		amount = taxable_income * 0.1 
	elif (taxable_income > 8350 and taxable_income <= 33950):
		balance = 8350 * 0.1
		
		deduction = (taxable_income - 8350) * 0.15

		amount = balance + deduction

	elif (taxable_income > 33950 and taxable_income <= 82250):
		balance = 8350 * 0.1
		secondBalance = 82250 - 33951
		deduction = (taxable_income - secondBalance) * 0.25
		amount = deduction + balance
		
	elif (taxable_income > 82250 and taxable_income <= 171550):
		amount = taxable_income * 0.33
	elif (taxable_income > 372950):
		amount = taxable_income * 0.35
print(amount)


