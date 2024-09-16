
balance = 0
user_choice = 0

while(user_choice != 4):
	menu = ("""

	>1> Deposit
	>2> Withdraw
	>3> Balance
	>4> Exit

	""")

	user_choice = int(input(menu))
	if (user_choice == 1):
		deposit = float(input("Enter deposit amount: "))
		balance += deposit

	elif (user_choice == 2):
		withdrawal = float(input("Enter withdrawal amount: "))
		if(withdrawal<balance):
			balance -= withdrawal
		else: 
			print("insufficient balance, make a deposit!!!")
	print("Your balance is N{:,.2f}".format(balance))
	

print("Thank you for banking with us")


#def withdrawal():
	#deposit = float(input("Enter deposit amount: ")
	#balance += deosit
	#return f'balance'
#for _ in range(10) ----to loop ten times without a variable name
#if you use while True:, let there be an elif statement e.g 
#elif (user_choice == 0): 
	#print("Your balance is N", balance)
	#break






