''' PSEUDO CODE =
1. request deposits from the user and store as deposits
2. request withdrawals from the user and store as withdrawal
3. let the user keep depositing and withdrawal until the user decides to stop
4. when the user decides to quit, display the output as net amount
'''

menu = ("""
1 ->> Deposit
2 ->> Withdraw
3 ->> Balance
0 ->> Quit

""")
option = int(input(menu))
balance = 0

while option != 0:

	if option == 1:
		amount_deposit = float(input("Enter amount to deposit: "))
		balance+=amount_deposit
		option = int(input(menu))


	elif option == 2:
		withdrawal_amount =  float(input("Enter amount to withdraw: "))

		if withdrawal_amount <= balance:

			balance -= withdrawal_amount

		else: 
			print("insufficient funds, make some deposits!!!")

		option = int(input(menu))

	elif option == 3:

		print("Your balance is ", balance)
		break
	else:
		print("sorry, you just entered an invalid number")
		break

print("Thank you for banking with us")

