for number in range(0,9,1):
	for digits in range(0,9-number):
		print(end=' ')
	for digits in range(0,number):
		print('*',end=' ')
	print()

for number in range(9,0,-1):
	print(f'{'*' * number}')
for number in range(1,9):
	print(f'{'*' * number}')
for number in range(0,9):
	print(f'{' ' * number}')
	
