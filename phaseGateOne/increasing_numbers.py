first_integer = int(input("Enter first integer: "))
second_integer = int(input("Enter second integer: "))
third_integer = int(input("Enter third integer: "))


largest_number = 0
second_largest_number = 0
smallest_number = 0



if(first_integer > second_integer and first_integer > third_integer):
	 largest_number = first_integer

elif(first_integer < second_integer and first_integer > third_integer):
	 second_largest_number = first_integer

elif(first_integer < second_integer and first_integer < third_integer):
	 smallest_number = first_integer

elif(second_integer > first_integer and second_integer > third_integer):
	 largest_number = second_integer

elif(second_integer > first_integer and second_integer < third_integer):
	 second_largest_number = second_integer

elif(second_integer < first_integer and second_integer < third_integer):
	 smallest_number = second_integer


elif(third_integer > first_integer and third_integer > second_integer):
	 largest_number = third_integer

elif(third_integer > first_integer and third_integer < second_integer):
	 second_largest_number = third_integer

elif(third_integer < first_integer and third_integer < second_integer):
	 smallest_number = third_integer

print(smallest_number, second_largest_number, largest_number,)


