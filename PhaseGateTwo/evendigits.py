numbers = []

for number in range(1000, 3001):
		
	first_number = number % 10
	first_number_extraction = number // 10
	second_number = first_number_extraction % 10
	second_number_extraction = first_number_extraction // 10
	third_number = second_number_extraction % 10
	third_number_extraction = second_number_extraction // 10
	fourth_number = third_number_extraction % 10

	if(first_number  % 2 == 0 and second_number  % 2 == 0 and third_number  % 2 == 0 and fourth_number % 2 == 0):
		numbers.append(number)
print(numbers)
		
	
	
	



