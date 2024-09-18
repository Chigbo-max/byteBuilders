sum = 0
for count in range(0, 10):
	scores = int(input("Enter score: "))
	if(scores % 2 == 0):
		sum+=scores
print("Sum is ", sum)

