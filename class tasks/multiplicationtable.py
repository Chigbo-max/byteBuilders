
'''PSEUDO CODE 
1. prompt the user for a number and store it.
2. print out numbers from 1 to 10
3. multiply the number given by the user by each printed number starting from 1 and at ten.
'''
prefered_number = float(input("Enter a number: "))
count = 1
for number in range(1, 11, 1):
	if (prefered_number  % number == 0):
		result = number * prefered_number 
		print(prefered_number, " x ",number, " = ",result)

	else:
		print(prefered_number , " x ",number, " = ", number*prefered_number )
