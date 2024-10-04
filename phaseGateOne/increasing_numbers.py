number_of_elements = int(input("Enter number of elements: "))

array = []

for _ in range(0,number_of_elements):
	number = int(input("Enter an integer: "))
	array.append(number)

for index in range(0, len(array)):
	for checker in range(1, len(array)):
		if(array[checker-1] > array[checker]):
			temp = array[checker-1]
			array[checker-1] = array[checker]
			array[checker] = temp
	
print(array)



