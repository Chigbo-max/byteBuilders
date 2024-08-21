'''
PSEUDO CODE

1.prompt the use to input three different numbers
2.store the first number as number one, second as number two and third as number three
3. sum up the values of step2
4. store the result as the sum of the three numbers
5. calculate the average of step 4.
6. display the result'''

'''number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

sum_of_three_numbers = number1 + number2 + number3
average = sum_of_three_numbers/3

print("The average of the three numbers is", round(average,2))
'''

number1, number2, number3 = map(int,input("Enter three numbers").split())
average = (number1 + number2 + number3)/3
print("The average of the three numbers is", round(average,2))
