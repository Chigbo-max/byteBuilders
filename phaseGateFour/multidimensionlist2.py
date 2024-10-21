try:

	row = int(input("Enter number of rows: "))
	column = int(input("Enter number of columns: "))

	'''
	digit = [0]
	digit *= column
	numbers = []


	for _ in range(row):
		numbers.append(digit)

	for row in range(len(numbers)):
		for column in range(len(numbers[row])):
			print(row * column, end=" ")
		print()
	'''

	if(row >= 0 and column >= 0):
		array = [[0]*column for _ in range(row)]

		for row in range(len(array)):
			for column in range(len(array[row])):
				print(f'{row * column:4}', end=" ")
			print()
	else:
		print("input cannot be less than zero")
except:
	TypeError(print("Invalid input"))