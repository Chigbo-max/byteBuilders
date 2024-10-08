unit = int(input("Enter number of units: "))

price = 0
if (unit > 100 and unit <= 200):
	price = (unit - 100) * 50
elif(unit > 200):
	price = (unit - 100) * 50
print(price)