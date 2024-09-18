

sum = 0
counter = 0

for count in range(0,10):
	scores = int(input("Enter score: "))
	if(scores >= 0 and scores <= 100):
		count+=1
		sum+=scores	
		counter+=1

print("Average is ", sum//counter)
				




