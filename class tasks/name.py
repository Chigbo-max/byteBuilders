'''
PSEUDO CODE
1. prompt the user to enter name
2. store the input as "name"
3. if the user enters a name, print the user's name with a message.
4. if the user fails to enter a number, tell the user that the input is invalid
'''

name = input("Enter name: ")

if name != '':
	print("hello, your name is ", name)
else:
	print("sorry, that's an invalid name, try again")


#space is a character
#python sees an empty space as a character

