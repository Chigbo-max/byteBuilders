amount_of_investment = float(input("Enter amount to invest: "))
number_of_years = int(input("Enter number of years: "))
percentage = float(input("Enter percentage: "))




if(amount_of_investment > 0 and number_of_years > 0 and percentage > 0):

	print(f'{"YEAR"}	 {"ROI"}		{"ACCRUED AMOUNT"}')

	for number in range(1, number_of_years + 1):

		accrued_amount = 0
	
		INTEREST_RATE = percentage / 100

		amount = amount_of_investment * INTEREST_RATE #100000
		
		accrued_amount = round(amount + amount_of_investment, 1)

		interest = round(accrued_amount - amount, 1)

		amount_of_investment = accrued_amount

			
		print(f'{number}	N{interest:,}	N{accrued_amount:,}')
else:
	print("invalid input, please enter a number from 1")


	