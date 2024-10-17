def get_swapped_elements(numbers):
	array = numbers
	for index in range(0, len(numbers)-1):
		temp = array[index]
		if(index % 2 == 0):
			array[index] = array[index + 1]
			array[index + 1] = temp
	return array
	
	