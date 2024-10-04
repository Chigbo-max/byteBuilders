import random

array = []
even_sum = 0
odd_sum = 0
multiplication = 1
average = 0
length = 0

for numbers in range(10):
	array.append(random.randrange(50))

	if(array[numbers] % 2 == 0):
		even_sum += array[numbers]

	if(array[numbers] % 2 != 0):
		odd_sum += array[numbers]
	
	if(numbers % 3 == 0):
		multiplication *= array[numbers]

	average = array[numbers] // 10

	length = length +1
	

	


print(even_sum)
print(odd_sum)
print(multiplication)
print(average)
print(length)

