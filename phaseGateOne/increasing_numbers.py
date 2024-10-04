number_of_elements = int(input("Enter number of elements: "))

array = []

for _ in range(0,number_of_elements):
	number = int(input("Enter an integer: "))
	array.append(number)

print(sorted(array))
print(sorted(array, reverse = True))


number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))

if number1 > number2:
	number1,number2 = number2,number1
if number1 > number3:
	number1, number3 = number3,number1

if number2 > number3:
	number2, number3 = number3, number2



print(number1, number2, number3)






