'''
PSEUDO CODE
1. prompt the user to enter name
2. store the input as "name"
3. if the user enters a name, print the user's name with a message.
4. if the user fails to enter a number, tell the user that the input is invalid
'''

MENU = '''
Select an option

1 ->> Phone book
2 ->> Messages
3 ->> Chat
4 ->> Call register
5 ->> Tones
6 ->> Settings
7 ->> Call divert
8 ->> Games
9 ->> Calculator
10 ->> Reminder
11 ->> Clock
12 ->> Profiles
13 ->> SIM services
'''
print(MENU)

			
menu_options = int(input("Enter a number: "))

if menu_options == 1:
	phone_book = '''
	1 ->> Search
	2 ->> Service Nos
	3 ->> Add name
	4 ->> Erase
	5 ->> Edit
	6 ->> Assign tone
	7 ->> Send b1 card
	8 ->> Options
	0 ->> Main menu		 
		'''
	print(phone_book)
	
	phone_book_options = int(input("Enter a number here: "))	
	
	if phone_book_options == 1:
		print("Search")
	
	elif phone_book_options == 2:
		print("Service Nos")
	
	elif phone_book_options == 3:
		print("Add name")
	
	elif phone_book_options == 4:
		print("Erase")

	elif phone_book_options == 5:
		print("Edit")

	elif phone_book_options == 6:
		print("Assign tone")
	
	elif phone_book_options == 7:
		print("Send b1 card")
	
	elif phone_book_options == 8:
		print("Options")
		options = '''
		1 ->> Type of view
		2 ->> Memory status
		0 ->> Previous menu
			'''
		options_sub_menu = int(input(options))
		if options_sub_menu == 1:
			print("Type of view")
			
		elif options_sub_menu == 2:
			print("Memory status")
		
		elif options_sub_menu == 0:
			input(phone_book)
		else:
			print("sorry, you just entered an invalid number")

	elif phone_book_options == 0:
		input(MENU)
	else:
		print("sorry, you just entered an invalid number")

if menu_options == 2:

	messages = '''
		1 ->> Write messages
		2 ->> Inbox
		3 ->> Outbox
		4 ->> Picture messages
		5 ->> Templates
		6 ->> Smiley
		7 ->> Message settings
		0 ->> Main menu
		'''
		print(messages)
		
		messages_options = int(input("Enter a number: "))
		
		if messages_options == 1:
			print("Write messages")
		elif messages_options == 2:
			print("Inbox")
		elif messages_options == 3:
			print("Outbox")
		elif messages_options == 4:
			print("Picture messages")
		elif messages_options == 5:
			print("Templates")
		elif messages_options == 6:
			print("Smiley")
		elif messages_options == 7:
			print("Message settings")
		elif messages_options == 0:
			print(MENU)
		else:
			print("sorry, you just entered an invalid number")

			
		
	
	
	
	


	










			



