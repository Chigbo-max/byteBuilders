sum = 0
counter = 0
for count in range(0, 10):
	scores = int(input("Enter score: "))
	counter+=1
	if(counter % 2 == 0):
		sum+=counter
print("Sum is ", sum)

