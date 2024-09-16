for number in range(0,9,1):
	for digits in range(0,9-number):
		print(end=' ')
	for digits in range(0,number):
		print('*',end=' ')
	print()