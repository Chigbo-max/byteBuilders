'''between 0 and 1000, the both exclusive... any value outside the range is seen as an invalid input, any value within the range should be calculated and the sum displayed if even and values subtracted if odd... however if one value is odd and the other, even the numbers should be skipped


def numbers_between_1000_and_0(number):

first_digit = number//100
second_digit = (number%100)//10
third_digit = number % 10

if(first_digit % 2 == 0 and second_digit % 2 == 0 and third_digit % 2 == 0):
even = first_digit + second_digit + third_digit
else:
even = (first_digit - second_digit - third_digit)

return even
			

print(numbers_between_1000_and_0(33))
'''




def numbers_between_1000_and_0(number):

	result = 0
	digit = 0

	while(number!=0):
		digit = number%10
		

		if (digit % 2 == 0):
			result = result + digit

		else:
			result = digit - result
		
		number = number // 10


	return result

print(numbers_between_1000_and_0(999))



#result = (result * 10) + (number%10)








