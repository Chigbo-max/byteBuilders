'''
PSEUDO CODE
1. create a function with three parameters (investment_amount,monthly-interest_rate, years)
2. name the function, future_investment
3. convert years into number of months(years *12) and assign to variable number_of_months
4. calculate the future investment with the formula, investment_amount * (1 + monthly_interest_rate) **number_of_months and assign to variable future_investment value
5. display result
6. handle negative values
7. handle string values

'''

def future_investment(investment_amount, monthly_interest_rate, years):
	
	if investment_amount < 0 or monthly_interest_rate < 0 or years < 0:
		raise ValueError("Invalid number")

	number_of_months = years * 12
	
	monthly_interest = monthly_interest_rate / 100
	
	future_investment_value = investment_amount * (1 + monthly_interest) **number_of_months

	return future_investment_value