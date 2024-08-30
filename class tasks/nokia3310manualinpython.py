'''
PSEUDO CODE
1. prompt the user to enter name
2. store the input as "name"
3. if the user enters a name, print the user's name with a message.
4. if the user fails to enter a number, tell the user that the input is invalid
'''

menu = '''
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
menu_options = int(input(menu))
while True:

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
	
		phone_book_options = int(input(phone_book))	
	
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
				int(input(phone_book))

			else:
				print("sorry, you just entered an invalid number, try again!")


		elif phone_book_options == 0:
			int(input(menu))
		else:
			print("sorry, you just entered an invalid number, try again!")
	
	if menu_options == 2:
		message = """
		1 ->> Write messages
		2 ->> Inbox
		3 ->> Outbox
		4 ->> Picture messages
		5 ->> Templates
		6 ->> Smiley
		7 ->> Message settings
		0 ->> Main menu
		"""
		message_options = int(input(message))
		
		if message_options == 1:
			print("Write messages")
	
		elif message_options == 2:
			print("Inbox")

		elif message_options == 3:
			print("Outbox")
	
		elif message_options == 4:
			print("Picture messages")
	
		elif message_options == 5:
			print("Templates")
	
		elif message_options == 6:
			print("Smiley")

		elif message_options == 7:
			message_settings = """
			1->> Set 1, 2
			2->> Common 3
			3->> Character support
			0->> Back
			"""

			message_setting_options = int(input(message_settings))
		
			if message_setting_options == 1:
				set_one_two = """
				1->> Message centre number
				2->> Message sent as
				3->> Message validity
				0->> Back

				"""
				set_one_two_options = int(input(set_one_two))
				if set_one_two_options == 1:
					print("Message centre number")
	
				elif set_one_two_options == 2:
					print("Message sent as")

				elif set_one_two_options == 3:
					print("Message validity")
	
				elif set_one_two_options == 0:
					int(input(message_settings))
				else:
					print("sorry, you just entered an invalid number, try again!")

				
				
			elif message_setting_options == 2:
				print("Common 3")

			elif message_setting_options == 3:
				print("Character support")
	
			elif message_setting_options == 0:
				int(input(message))
			else:
				print("sorry, you just entered an invalid number, try again!")

		elif message_options == 0:
			int(input(menu))

		else:
			print("sorry, you just entered an invalid number, try again!")

	if menu_options == 3:
		print("Chat")
	
	if menu_options == 4:
		call_register = """
			1->> Missed calls
			2->> Received calls
			3->> Dialled numbers
			4->> Erase recent call lists
			5->> Show call duration
			6->> Show call cost
			7->> Call cost settings
			8->> Prepaid cost
			"""
		call_register_options = int(input(call_register))
		
		if call_register_options == 1:
			print("Missed calls")
	
		elif call_register_options == 2:
			print("Received calls")

		elif call_register_options == 3:
			print("Dialled numbers")
	
		elif call_register_options == 4:
			print("Erase recent call lists")

		elif call_register_options == 5:

			call_duration = """
			1->> Last call duration
			2->> All calls' duration
			3->> Received calls' duration
			4->> Dialled calls' duration	
			5->> Clear timers
			0->> Back	
			"""
			call_duration_options = int(input(call_duration))
			
			if call_duration_options == 1:
				print("Last call duration")
	
			elif call_duration_options == 2:
				print("All calls' duration")

			elif call_duration_options == 3:
				print("Received calls' duration")
	
			elif call_duration_options == 4:
				print("Dialled calls' duration")

			elif call_duration_options == 5:
				print("Clear timers")

			elif call_duration_options == 0:
				int(input(call_register))

			else:
				print("sorry, you just entered an invalid number, try again!")
			

		elif call_register_options == 6:
			call_cost = """
			1->> Last call cost
			2->> All calls' cost
			3->> Clear counters
			4->> Back	
			"""
			call_cost_options = int(input(call_cost))
			
			if call_cost_options == 1:
				print("Last call cost")
	
			elif call_cost_options == 2:
				print("All calls' cost")

			elif call_cost_options == 3:
				print("Clear counters")

			elif call_cost_options == 0:
				int(input(call_register))

			else:
				print("sorry, you just entered an invalid number, try again!")


		elif call_register_options == 7:
			call_cost_settings = """
			1->> Call cost limit
			2->> Show costs in
			3->> Back
			"""
			call_cost_settings_options = int(input(call_cost_settings))
			if call_cost_options == 1:
				print("Call cost limit")

			elif call_cost_options == 2:
				print("Show costs in")

			elif call_cost_options == 0:
				int(input(call_register))
			else:
				print("sorry, you just entered an invalid number, try again!")



		elif call_register_options == 8:
			print("Prepaid cost")
	
		elif call_register_options == 0:
			int(input(menu))

		else:
			print("sorry, you just entered an invalid number, try again!")


	if menu_options == 5:

		tones = '''
		1->> Ringing Tone
		2->> Ringing volume
		3->> Incoming call alert
		4->> Composer
		5->> Message alert tone
		6->> Keypad tones
		7->> Warning game tones
		8->> Vibrating alert
		9->> Screen saver
		0->> Main menu
		'''
		tones_options = int(input(tones))

		if tones_options == 1:
			print("Ringing Tone")
	
		elif tones_options == 2:
			print("Ringing volume")

		elif tones_options == 3:
			print("Incoming call alert")
	
		elif tones_options == 4:
			print("Composer")

		elif tones_options == 5:
			print("Message alert tone")

		elif tones_options == 6:
			print("Keypad tones")

		elif tones_options == 7:
			print("Warning game tones")
	
		elif tones_options == 8:
			print("Vibrating alert")

		elif tones_options == 9:
			print("Screen saver")

		elif tones_options == 0:
			int(input(menu))

		else:
			print("sorry, you just entered an invalid number, try again!")

	if menu_options == 6:

		settings = """
		1->> Call settings
		2->> Phone settings
		3->> Security settings
		4->> Restore factory settings
		0->> Main menu			
		"""
		settings_options = int(input(settings))
	
		if settings_options == 1:

			call_settings = """			
			1->> Automatic redial
			2->> Speed dial
			3->> Call waiting options
			4->> Own number sending
			5->> Phone line in use
			6->> Automatic answer
			0->> Back
			"""
			call_settings_options = int(input(call_settings))

			if call_settings_options == 1:
				print("Automatic redial")
	
			elif call_settings_options == 2:
				print("Speed dial")

			elif call_settings_options == 3:
				print("Call waiting options")
	
			elif call_settings_options == 4:
				print("Own number sending")

			elif call_settings_options == 5:
				print("Phone line in use")

			elif call_settings_options == 6:
				print("Automatic answer")

			elif call_settings_options == 0:
				int(input(settings))
			else:
				print("sorry, you just entered an invalid number, try again!")


		elif settings_options == 2:
			phone_settings = """
			
			1->> Language
			2->> Cell into display
			3->> Welcome note
			4->> Network selection
			5->> Lights
			6->> Confirm SIM service actions
			0 ->> Back
			"""
			phone_settings_options = int(user(phone_settings))
			
			if phone_settings_options == 1:
				print("Language")
	
			elif phone_settings_options == 2:
				print("Cell into display")

			elif phone_settings_options == 3:
				print("Welcome note")
	
			elif phone_settings_options == 4:
				print("Network selection")

			elif phone_settings_options == 5:
				print("Lights")

			elif phone_settings_options == 6:
				print("Confirm SIM service actions")

			elif phone_settings_options == 0:
				int(input(settings))
			else:
				print("sorry, you just entered an invalid number, try again!")
			


		elif settings_options == 3:
			security_settings = """		
				1->> PIN code request
				2->> Call baring service
				3->> Fixed calling
				4->> Closed user group
				5->> Phone security
				6->> Change access codes
				0->> Back
				""";
			security_settings_options = int(input(security_settings))
				
			if security_settings_options == 1:
				print("PIN code request")
	
			elif security_settings_options == 2:
				print(" Call baring service")

			elif security_settings_options == 3:
				print("Fixed calling")
	
			elif security_settings_options == 4:
				print("Closed user group")

			elif security_settings_options == 5:
				print("Phone security")

			elif security_settings_options == 6:
				print("Change access codes")

			elif security_settings_options == 0:
				int(input(settings))
			else:
				print("sorry, you just entered an invalid number, try again!")

		elif settings_options == 4:
			print("Restore factory settings")

		elif settings_options == 0:
			int(input(menu))
		
		else:
			print("sorry, you just entered an invalid number, try again!")


	if menu_options == 7:
		print("Call divert")

	if menu_options == 8:
		print("Games")

	if menu_options == 9:
		print("Calculator")
	
	if menu_options == 10:
		print("Reminders")

	if menu_options == 11:

		clock = """
		1 ->> Alarm clock
		2 ->> Clock settings
		3 ->> Date settings
		4 ->> StopWatch
		5 ->> Countdown timer
		6 ->> Auto update of date and time
		0 ->> Main menu
		"""
		clock_options = int(input(clock))
		
		if clock_options == 1:
			print("Alarm clock")

		elif clock_options == 2:
			print("Clock settings")

		elif clock_options == 3:
			print("Date settings")

		elif clock_options == 4:
			print("StopWatch")

		elif clock_options == 5:
			print("Countdown timer")

		elif clock_options == 6:
			print("Auto update of date and time")

		elif clock_options == 0:
			int(input(menu))

		else:
			print("sorry, you just entered an invalid number, try again!")


	if menu_options == 12:
		print("Profiles")
	
	if menu_options == 13:
		print("SIM services")
	break
	








