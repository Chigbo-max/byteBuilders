number = int(input("Enter a number between 0 and 1000: "))

thousand = number % 10
extracted_thousand = number // 10
hundred = extracted_thousand % 10
extracted_hundred = extracted_thousand // 10
ten = extracted_hundred % 10
last = number // 1000

sum = thousand + hundred + ten + last

print(sum)

firstNumber = 2
secondNumber = 3
for number in range(1, 3):
	number += firstNumber
for numbers in range(1,4):
	numbers += secondNumber
print(number)
print(numbers)
	