import random

guess = input("Enter three different numbers by a space: ")

words = guess.split(" ")


first_random = str(random.randrange(2))
second_random = str(random.randrange(1))
third_random = str(random.randrange(2))

print(first_random, end=" ")
print(second_random, end=" ")
print(third_random, end=" ")
print()



if(words[0] == first_random and words[1] == second_random and words[2] == third_random): print("You've won $5,000!")

elif(words[0] == second_random and words[1] == third_random and words[2] == first_random): print("You've won $4,000! You're close to Gold!")


elif(words[0] == third_random and words[1] == first_random and words[2] == second_random): print("You've won $4,000!, You're close to Gold!")

elif(words[0] == first_random and words[1] != second_random and words[2] == third_random): print("You've won $3,000, but you can do better!")

elif(words[0] == first_random and words[1] != second_random and words[2] != third_random): print("You've won $3,000, but you can do better!")

elif(words[0] != first_random and words[1] == second_random and words[2] == third_random): print("You've won $3,000, but you can do better!")

elif(words[0] == first_random and words[1] == second_random and words[2] != third_random): print("You've won $3,000, but you can do better!")

elif(words[0] != first_random and words[1] != second_random and words[2] == third_random): print("You've won $2,000, but you can do better!")

elif(words[0] == first_random and words[1] != second_random and words[2] != third_random): print("You've won $2,000, but you can do better!")

elif(words[0] != first_random and words[1] == second_random and words[2] != third_random): print("You've won $2,000, but you can do better!")

elif (words[0] != first_random and words[1] != second_random and words[2] != third_random): print("oops, nice try! Give it your best shot next time!")







