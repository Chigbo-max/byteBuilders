
number = int(input("Enter a number: "))

def reverse(number):
	reverse = 0
	while(number != 0):
		reverse = (reverse * 10) + (number % 10)
		number = number//10
	return reverse
reverse(number)



def is_palindrome(number):
	if(reverse(number) == number):
		return print("Number is a palindrome")
	else:
		return print("Number is not a palindrome")
is_palindrome(number)


		