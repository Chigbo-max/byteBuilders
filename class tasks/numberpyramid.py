choice = int(input("Enter a number: "))

for number in range(1, choice, 1):
	for pyramid in range(number, choice, 1):
		print(pyramid, end=' ')
	print(" ")
