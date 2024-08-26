'''message = Go placidly amidst the noise and haste and remember what peace there may be in silence. As far as possible without surrender, be on good terms will all persons'. Speak your truth quietly and clearly. Even the dull and ignorant, they too have their story.

print(message)


score = int(input("Enter a number: "))

result = "failed"
if score >= 40:
	result = "passed"
	print("really passed")

print(result)

score = int(input("Enter a number: "))

result = " "

if score >= 40:
	result = "passed"
	print(result)

if score <= 40:
	result = "failed"
	print(result)

#score = int(input("Enter a number: "))

#if score >= 40:
	#print("passed")

'''
number = int(input("Enter a three-digit number: "))

hundred = number // 100
remainder = number % 100
ten = remainder % 10 

if hundred==ten:
	print("number is a palindrome")
else:
	print("number is not a palindrome")




