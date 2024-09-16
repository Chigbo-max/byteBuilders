trips = float(input("Enter number of trips: "))

total_miles = 0
total_gallons = 0

counter = 1
	
while(counter <= trips):
	counter+=1

	miles_driven = int(input("Enter number of miles driven: "))
	total_miles += miles_driven
	
	gallons_used = int(input("Enter number of gallons used: "))
	total_gallons += gallons_used
	
	
combined_miles_per_gallon = total_miles / total_gallons
	
print("Combined miles per gallon: ", combined_miles_per_gallon)

