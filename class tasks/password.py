'''
PSEUDO CODE

1. Prompt the user to enter a password
2. store the input as password
3. count the number of character
4. assign asteriks to each of the character typed
5. print the result as asteriks

'''

password = input("Enter your password: ")
password_count = len(password)
password_asteriks = password_count * "*"
print("Your password: ", password_asteriks)