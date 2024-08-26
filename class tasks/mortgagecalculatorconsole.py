'''
PSEUDO CODE:
1. Prompt the user to enter the amount to borrow
2. store step 1 as principal
3. Prompt the user to enter the duration of the mortgage in years
4. store step 3 as duration
5. prompt the user to enter the yearly interest rate offered on the mortgage
6. store step 5 as annual interest rate
7. multiply step 4 by 12 months
8. store step 7 as the calculated duration
9. multiply step 6 by percentage and divide the result by 12
10. store step 9 as the calculated monthly interest rate
11. perform a calculation where 1 is added to step 10 and the result is raised to the power of step 8
12. multiply step 11 by step 10
13. perform the calculation in step 11 again and subtract 1 from the result
14. divide the result of step 12 by the result of step 13
15. multiply the result of step 14 by the principal(step 2)
17. if the user enters a principal amount less than zero, do not print result.
'''


principal = float(input("Please enter the amount you wish to borrow: "))

duration = float(input("Please enter the duration in years: "))

annual_interest_rate = float(input("Please enter the yearly interest rate: "))

MONTH_IN_YEARS = 12

PERCENTAGE = 0.01

calculated_duration = duration * 12
	
calculated_monthly_interest_rate = (annual_interest_rate * 0.01) / 12

if principal < 0:
	print("sorry you entered an invalid amount, try again")
else:
	
	monthly_mortgage_payment_calculation = (((calculated_monthly_interest_rate + 1) ** calculated_duration) *calculated_monthly_interest_rate)/(((calculated_monthly_interest_rate + 1) 	** calculated_duration)  - 1)
		
	monthly_mortgage_payment = principal * (monthly_mortgage_payment_calculation)


	print("Your monthly payment is $", round(monthly_mortgage_payment, 2));

