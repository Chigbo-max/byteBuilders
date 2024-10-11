import random

guess = input("Enter three different numbers by a space: ")

words = guess.split(" ")

print(words)

first_random = str(random.randrange(2))
second_random = str(random.randrange(1))
third_random = str(random.randrange(2))


if(words[0] == first_random and words[1] == second_random and words[2] == third_random): print("You've won $5,000")

elif(words[0] == second_random and words[1] == third_random and words[2] == first_random): print("You've won $4,000")

elif(words[0] == third_random and words[1] == first_random and words[2] == second_random): print("You've won $4,000")

elif(words[0] == first_random and words[1] != second_random and words[2] != third_random): print("You've won $3,000")

elif(words[0] != first_random and words[1] == second_random and words[2] == third_random): print("You've won $3,000")

elif(words[0] == first_random and words[1] == second_random and words[2] != third_random): print("You've won $3,000")

elif(words[0] != first_random and words[1] != second_random and words[2] == third_random): print("You've won $2,000")






