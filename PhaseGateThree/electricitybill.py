try:
	unit = int(input("Enter number of units: "))

	price = 0

	if(unit < 0):
		price = unit * 50
	if(unit > 0 and unit <=100):
		print("no charge")
	if (unit > 100 and unit <= 200):
		price =  (unit -100) * 50
	elif(unit > 200):
		price = (100*50) + (unit - 200) *100
	print(price)

except ValueError:
	print("invalid input")
