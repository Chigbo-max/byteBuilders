def display_largest(list):
	
	if not list:
		raise ValueError("List cannot be empty")
	list = [6]
	
	largest = list[0]
	for number in range(len(list)):
		if (list[number] > largest):
			largest = list[number] 
	return largest

def display_reverse(list):
	if not list:
		raise ValueError("List cannot be empty")
	list =[1,2,3,4,5]
	list.reverse()
	return list

def display_number_occurence_check(numbers):
	if not numbers:
		raise ValueError("List cannot be empty")
	numbers = [1,2,3,4,5]
	check = 3

	for number in range(len(numbers)):
		if check == number:
			return check

def display_odd_elements(numbers):

	if not numbers:
		raise ValueError("List cannot be empty")

	numbers = [1,2,3,4,5]
	
	for count in range(len(numbers)):
		if count % 2 != 0:
			return(numbers[count])

def display_even_elements(numbers):

	if not numbers:
		raise ValueError("List cannot be empty")

	numbers = [1,2,3,4,5]
	
	for count in range(len(numbers)):
		if count % 2 == 0:
			return(numbers[count])

def display_running_total(numbers):
	numbers = [1,2,3,4,5]
	runningTotal = 0
	for count in range(len(numbers)):
		runningTotal += numbers[count]
		return(runningTotal)

def display_string_palindrome(strings):
	strings = 'abcde'
	strings.reverse()	
	return strings
			


