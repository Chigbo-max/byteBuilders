numbers = []
sum = 0
count = 0
while True:
	number = int(input("Enter a number or 0 to quit: "))
	if number != 0:
		sum += number
		numbers += [number]
	if(number == 0):
		break
	count += 1
	average = sum/count
print(numbers)
print(average)
	
