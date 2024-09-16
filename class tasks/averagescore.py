'''average score of students in a class
collect scores of the students
get the number of students in a class
print the average
'''


def display_average():

	number_of_students = int(input("Enter number of students: "))

	student_count = 0
	total_student_score = 0
	

	while(student_count < number_of_students):

		student_score = int(input("Enter student score: "))
		total_student_score += student_score
		student_count+=1
	

	if (number_of_students == 0):
		return print("Error: number of students cannot be zero, try again")
	else:
		average = total_student_score // number_of_students
	
	print("The average score of students is:",average)

display_average()
