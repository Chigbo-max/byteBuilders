print(
'''
0 single fliers
1 married filling jointly
2 married filling separately
3 head of household

''')
try:
	userInput = int(input("Enter number: "))
	
	if(userInput != 0 and userInput != 1 and userInput !=2 and userInput !=3):
		print("invalid input: enter a number from 0-3")
		

	if (userInput == 0):
		
		taxable_income = float(input("Enter income: "))
		
		amount = 0

		if (taxable_income < 0): 
			print ("invalid input")

		if (taxable_income >= 0 and taxable_income <= 8350):
			amount = 8350 * 0.1 

		elif (taxable_income >= 8351 and taxable_income <= 33950):
			amount = (8350 * 0.1) + (taxable_income - 8351) * 0.15

		elif (taxable_income >= 33951 and taxable_income <= 82250):
			amount = (8350 * 0.1) + (33950 - 8351) * 0.15 + (taxable_income - 33951) * 0.25

		elif (taxable_income >= 82251 and taxable_income <= 171550):
			amount = (8350 * 0.1) + (33950 - 8351) * 0.15 + (82250 - 33951) * 0.25 + (taxable_income - 82251) * 0.28

		elif (taxable_income >= 171551 and taxable_income <= 372950):
			amount = (8350 * 0.1) + (33950 - 8351) * 0.15 + (82250 - 33951) * 0.25 + (171550 - 82251) * 0.28 + (taxable_income - 171551) * 0.33

		elif (taxable_income > 372950):
			amount = (8350 * 0.1) + (33950 - 8351) * 0.15 + (82250 - 33951) * 0.25 + (171550 - 82251) * 0.28 + (372950 - 171551) * 0.33 + (taxable_income - 372950) * 0.35

		print(f'${amount:,}')

	elif (userInput == 1):
		taxable_income = float(input("Enter income: "))

		amount = 0

		if (taxable_income < 0): 
			print ("invalid input")

		if (taxable_income >= 0 and taxable_income <= 16700):
			amount = 16700 * 0.1 

		elif (taxable_income >= 16701 and taxable_income <= 67900):
			amount = 16700 * 0.1 + (taxable_income - 16701) * 0.15

		elif (taxable_income >= 67901 and taxable_income <= 137050):
			amount = 16700 * 0.1 + (67900 -16701) * 0.15 + (taxable_income - 67901)*0.25

		elif (taxable_income >= 137051 and taxable_income <= 208850):
			amount = 16700 * 0.1 + (67900 - 16701) * 0.15 + (137050 - 67901) * 0.25 + (taxable_income - 137051) * 0.28
	
		elif (taxable_income >= 208851 and taxable_income <= 372950):
			amount = 16700 * 0.1 + (67900 - 16701) * 0.15 + (137050 - 67901) * 0.25 + (208850 - 137051) * 0.28 + (taxable_income - 208851)*0.33
		elif(taxable_income > 372950):
			amount = 16700 * 0.1 + (67900 - 16701) * 0.15 + (137050 - 67901) * 0.25 + (208850 - 137051) * 0.28 + (372950 - 208851) * 0.33 + (taxable_income - 372950) * 0.35
			print(f'${amount:,}')



	elif(userInput == 2):
		taxable_income = float(input("Enter income: "))

		amount = 0


		if (taxable_income < 0): 
			print ("invalid input")
	
		if(taxable_income >= 0 and taxable_income <= 8350):
			amount = 8350 * 0.1
	
		elif(taxable_income >= 8351 and taxable_income <= 33950):
			amount = 8350 * 0.1 + (taxable_income - 8351)*0.15
	
		elif(taxable_income >= 33951 and taxable_income <= 68525):
			amount = 8350 * 0.1 + (33950 - 8351) * 0.15 + (taxable_income - 33951)* 0.25
	
		elif(taxable_income >= 68526 and taxable_income <= 104425):
			amount = 8350 * 0.1 + (33950 - 8351) * 0.15 + (104425 - 68526)*0.25 + (taxable_income - 68526) * 0.28

		elif(taxable_income >= 104426 and taxable_income <= 186475):
			amount = 8350 * 0.1 + (33950 - 8351) * 0.15 + (104425 - 68526) * 0.25 + (104425 - 68526)* 0.28 + (taxable_income - 104426)*0.33

		elif(taxable_income > 186476):
			amount = 8350 * 0.1 + (33950 - 8351) * 0.15 + (104425 - 68526) * 0.25 + (104425 - 68526) * 0.28 + (186475 - 104426)*0.33 + (taxable_income - 186476)*0.35

		print(f'${amount:,}')


	elif(userInput == 3):
		taxable_income = float(input("Enter income: "))

		amount = 0


		if (taxable_income < 0): 
			print ("invalid input")

		if(taxable_income >=0 and taxable_income <= 11950):
			amount = 11950 * 0.1
	
		elif(taxable_income >= 11951 and taxable_income <= 45500):
			amount = 11950 * 0.1 + (taxable_income - 11951)*0.15
	
		elif(taxable_income >= 45501 and taxable_income <= 117450):
			amount = 11950 * 0.1 + (45500 -11951)*0.15 + (taxable_income - 45501)*0.25
	
		elif(taxable_income >= 117451 and taxable_income <= 190200):
			amount = 11950 * 0.1 + (45500 - 11951)*0.15 + (117450 - 45501)*0.25 + (taxable_income - 117451)*0.28

		elif(taxable_income >= 190201 and taxable_income <= 372950):
			amount = 11950 * 0.1 + (45500 - 11951)*0.15 + (117450 - 45501)*0.25 + (190200 - 117451)*0.28 + (taxable_income - 190201)* 0.33

		elif(taxable_income > 372950):
			amount = 11950 * 0.1 + (45500-11951)*0.15 + (117450 - 45501)*0.25 + (190200 - 117451)*0.28 + (372950 - 190201)*0.33 + (taxable_income - 372950)*0.35
		print(f'${amount:,}')

except ValueError:
	print("Invalid input")

	

	
	



