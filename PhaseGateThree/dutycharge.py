cost_of_car = float(input("Enter cost of car: "))

duty_charge = 0

if(number < 0 ):
	number = -(number)

if(cost_of_car > 10_000_000):
	duty_charge = cost_of_car * 0.2

elif(cost_of_car >= 5_000_000 and cost_of_car <= 10_000_000):
	duty_charge = cost_of_car * 0.15

elif(cost_of_car >= 2_500_000 and cost_of_car <= 5_000_000):
	duty_charge = cost_of_car * 0.1

elif(cost_of_car < 2_500_000):
	duty_charge = cost_of_car * 0.5

print(duty_charge)
	
	