


sum = 0
count = 0

while(count >= 0):
	scores = int(input("Enter score: "))
	if(scores >= 0 and scores <= 100):
		count+=1
		sum+=scores			
	if(count == 10):
	
		print("Sum is ",sum)
		break
				




