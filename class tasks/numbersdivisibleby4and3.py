counter = 0
for number in range(101, 500, 1):
	if(number % 3 == 0 and number % 4 == 0):
		print(number, end = " ")
		counter+=1
		if(counter % 10 == 0):		
			print()	
