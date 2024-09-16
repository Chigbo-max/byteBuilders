'''miles = 175
kilometers = miles * 1.609
print(kilometers)



request for the budget
store it ina variable as the total budget
initialize the assumed price to 855
store it in a variable as price
divide the total budget by the price
display result
'''

for number in range(1, 10, 1):
	print(f'{number*'*':<12} {(number) * '*' + ' '* 3}')

total_budget = float(input("Enter budget: "))
PRICE = 855
number_of_liters = total_budget / PRICE
print("Number of liters to purchase= ", round(number_of_liters, 2))
