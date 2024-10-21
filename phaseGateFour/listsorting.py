array = [5, 2, 7, 2, 8, 2, 3, 4, 6]

def display_ascending_order(array):
	for index in range(0, len(array)):
		for checker in range(1, len(array)):
			if(array[checker] < array[checker - 1]):
				temp = array[checker - 1]
				array[checker - 1] = array[checker]
				array[checker] = temp
	return array
print(display_ascending_order(array))			
	

def display_descending_order(array):
	for index in range(0, len(array)):
		for checker in range(1, len(array)):
			if(array[checker] > array[checker - 1]):
				temp = array[checker - 1]
				array[checker - 1] = array[checker]
				array[checker] = temp
	return array
print(display_descending_order(array))	


def display_multiplication_of_elements_at_third_positions(array):
	product = 1
	for index in range(2,len(array), 3):
		product *= array[index]
	return product
print(display_multiplication_of_elements_at_third_positions(array))


def display_squared_elements(array):
	
	for index in range(len(array)):
		array[index] *= array[index]
	return array
print(display_squared_elements(array))	



			




