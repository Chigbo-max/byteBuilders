def menu():

	print("""
		
	12 DAYS OF CHRISTMAS LYRICS

	""")

	choice = int(input("Enter a number from 1 to 12:"))
	
	match(choice):
		case 1: 
			first_day_of_christmas()

		case 2:
			second_day_of_christmas()
		case 3:
			third_day_of_christmas()
		case 4: 
			fourth_day_of_christmas()
		case 5: 
			fifth_day_of_christmas()
		case 6:
			sixth_day_Of_christmas()
		case 7: 
			seventh_day_of_christmas()
		case 8:
			eight_day_of_christmas()
		case 9:
			ninth_day_of_christmas()
		case 10:
			tenth_day_of_christmas()
		case 11:
			eleventh_day_of_christmas()
		case 12:
			twelfth_day_of_christmas()
		case _: 
			print("oops, you entered an invalid number, try again")
			menu()
		
def first_day_of_christmas():

	print("""
		
	On the first day of Christmas, my true love sent to me
	A partridge in a pear tree

	""")
	first_day = int(input("Press 1 to go back: "));
		
	match(first_day):
		case 1: 
			menu()
		case _:
			print("oops, you entered an invalid number, try again")
	
def second_day_of_christmas():

	print("""
		
	On the second day of Christmas, my true love sent to me
	Two turtle doves and
	A partridge in a pear tree

	""")
	second_day = int(input("Press 1 to go back: "))
		
	match(second_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")
		

def third_day_of_christmas():

	print("""
		
	On the third day of Christmas, my true love sent to me
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")
	third_day = int(input("Press 1 to go back: "))
		
	match(third_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")
		

def fourth_day_of_christmas():

	print("""
		
	On the fourth day of Christmas, my true love sent to me
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")
	fourth_day = int(input("Press 1 to go back: "))
		
	match(fourth_day):
		case 1:
			menu()
		case _:
			print("oops, you entered an invalid number, try again")
		

def fifth_day_of_christmas():

	print("""
		
	On the fifth day of Christmas, my true love sent to me
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")
		
	fifth_day = int(input("Press 1 to go back: "))
		
	match(fifth_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an inavalid number, try again")
		

def sixth_day_Of_christmas():

	print("""
		
	On the sixth day of Christmas, my true love sent to me
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")
	sixth_day = int(input("Press 1 to go back: "))
		
	match(sixth_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an inavalid number, try again")
		


def seventh_day_of_christmas():

	print("""
		
	On the seventh day of Christmas, my true love sent to me
	Seven swans a-swimming
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")

	seventh_day = int(input("Press 1 to go back: "))
		
	match(seventh_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")
		
		


def eight_day_of_christmas():

	print("""
		
	On the eighth day of Christmas, my true love sent to me
	Eight maids a-milking
	Seven swans a-swimming
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")
	eight_day = int(input("Press 1 to go back: "))
		
	match(eight_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")


def ninth_day_of_christmas():

	print("""
		
	On the ninth day of Christmas, my true love sent to me
	Nine ladies dancing
	Eight maids a-milking
	Seven swans a-swimming
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

	""")
	ninth_day = int(input("Press 1 to go back: "))
		
	match(ninth_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")
		

		
def tenth_day_of_christmas():

	print("""
		
	On the tenth day of Christmas, my true love sent to me
	Ten lords a-leaping
	Nine ladies dancing
	Eight maids a-milking
	Seven swans a-swimming
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree

		""")
	tenth_day = int(input("Press 1 to go back: "))
		
	match(tenth_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")
		
	

			
def eleventh_day_of_christmas():

	print("""
		
	On the eleventh day of Christmas, my true love sent to me
	Eleven pipers piping
	Ten lords a-leaping
	Nine ladies dancing
	Eight maids a-milking
	Seven swans a-swimming
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hens
	Two turtle doves and
	A partridge in a pear tree
		
	""")

	eleventh_day = int(input("Press 1 to go back: "))
		
	match(eleventh_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")
		

			
def twelfth_day_of_christmas():

	print("""

	On the twelfth day of Christmas, my true love sent to me
	Twelve drummers drumming
	Eleven pipers piping
	Ten lords a-leaping
	Nine ladies dancing
	Eight maids a-milking
	Seven swans a-swimming
	Six geese a-laying
	Five golden rings
	Four calling birds
	Three french hen
	Two turtle doves and
	A partridge in a pear tree

	""")
	twelfth_day = int(input("Press 1 to go back: "))
		
	match(twelfth_day):
		case 1:
			 menu()
		case _:
			print("oops, you entered an invalid number, try again")


menu()		


