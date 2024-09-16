preferred_number = int(input("Enter a number: "))


for number in range(preferred_number,0,-1):
	for digits in range(0,preferred_number):
		print(end=' ')
	for digits in range(1, number):
		print(digits,end=' ')
	print()