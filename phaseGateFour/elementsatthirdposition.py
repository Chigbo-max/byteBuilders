digits = [5, 2, 7, 1, 8, 2]

def display_multiplication_of_elements_at_third_positions(digits):
	product = 1
	for index in range(0,len(digits), 3):
		product *= digits[index]
	return product
print(display_multiplication_of_elements_at_third_positions(digits))
