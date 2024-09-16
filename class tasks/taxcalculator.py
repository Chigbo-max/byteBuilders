first_citizen_earnings = float(input("Enter earnings for the first citizen: "))

second_citizen_earnings = float(input("Enter earnings for the second citizen: "))

third_citizen_earnings = float(input("Enter earnings for the third citizen: "))



if(first_citizen_earnings <= 30000):
	first_citizen_earnings = 0.15 * first_citizen_earnings
else:
	first_citizen_earnings = 0.2 * first_citizen_earnings

if(second_citizen_earnings <= 30000):
	second_citizen_earnings = 0.15 * second_citizen_earnings
else:
	second_citizen_earnings = 0.2 * second_citizen_earnings

if(third_citizen_earnings <= 30000):
	third_citizen_earnings = 0.15 * third_citizen_earnings

else: 
	third_citizen_earnings = 0.2 * third_citizen_earnings
	

print("The total tax for the first citizen is: $", first_citizen_earnings)

print("The total tax for the second citizen is: $", second_citizen_earnings)

print("The total tax for the third citizen is: $", third_citizen_earnings)

