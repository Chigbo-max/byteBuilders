array = [[0] * 4 for _ in range(5)]
for row in range (len(array)):
	for column in range (len(array[row])):
		print(array[row][column], end = " ")
	print()



digits = [0]
digits*=4 #column #5 is the row
array = []

for _ in range(5):
	array.append(digits)
print(array)

for row in range(len(array)):
	for column in range(len(array[row])):
		print(array[row][column] * row, end=" ")
	print()
	


	

