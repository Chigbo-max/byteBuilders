import math

menu = """

MENU

Select your preferred option

1-> Sapa size - 4 slices - 2k per box

2-> Small money - 6 slices - 2.4k per box

3-> Big boys - 8 slices - 3k per box

4-> Odogwu - 12 slices - 4.2k per box

"""

customer_choice = int(input(menu))

match customer_choice:
	case 1 : 

		print("Sapa Size")
		
		number_of_guests = float(input("Enter number of guests: "))
		sapa_price = 2000;
		number_of_sapa_slices = 4
		number_of_sapa_slices_left = 0
		
		
		number_of_boxes = math.ceil(number_of_guests / number_of_sapa_slices)
		print("Number of boxes to buy = ", number_of_boxes)
		
		number_of_sapa_slices_left = (number_of_sapa_slices *  number_of_boxes) - number_of_guests
		print("Number of slices left = ", number_of_sapa_slices_left)

		
		total_price = number_of_boxes * sapa_price
		print("Price = ", total_price)

		
	case 2 :

		print("Small Money")

		number_of_guests = float(input("Enter number of guests: "))
		small_money_price = 2400;
		number_of_small_money_slices = 6
		number_of_small_money_slices_left = 0

		
		number_of_boxes = math.ceil(number_of_guests / number_of_small_money_slices)
		print("Number of boxes to buy = ", number_of_boxes)
		
		number_of_small_money_slices_left = (number_of_small_money_slices *  number_of_boxes) - number_of_guests
		print("Number of slices left = ", number_of_small_money_slices_left)

		
		total_price = number_of_boxes * small_money_price
		print("Price = ", total_price)
		
		
		
	case 3 :

		print("Big Boys")

		number_of_guests = float(input("Enter number of guests: "))
		big_boys_price = 3000;
		number_of_big_boys_slices = 8
		number_of_big_boys_slices_left = 0

		
		number_of_boxes = math.ceil(number_of_guests / number_of_big_boys_slices)
		print("Number of boxes to buy = ", number_of_boxes)
		
		number_of_big_boys_slices_left = (number_of_big_boys_slices *  number_of_boxes) - number_of_guests
		print("Number of slices left = ", number_of_big_boys_slices_left)

		
		total_price = number_of_boxes * big_boys_price
		print("Price = ", total_price)

		
	case 4 :

		print("Odogwu")

		number_of_guests = float(input("Enter number of guests: "))
		odogwu_price = 4200;
		number_of_odogwu_slices = 12
		number_of_odogwu_slices_left = 0

		
		number_of_boxes = math.ceil(number_of_guests / number_of_odogwu_slices)
		print("Number of boxes to buy = ", number_of_boxes)
		
		number_of_odogwu_slices_left = (number_of_odogwu_slices *  number_of_boxes) - number_of_guests
		print("Number of slices left = ", number_of_odogwu_slices_left)

		
		total_price = number_of_boxes * odogwu_price 
		print("Price = ", total_price)



'''
PSEUDO CODE:

1.request for the number of people to be served
2.request for the pizza type
3.if customer selects the pizza type, divide the number of guests by the number of slices and store the result as the number of boxes to buy.
4.multiply the number of slices by the number of boxes, subtract the result from the number of guests, store the result as number of slices left.
5.multiply the number of boxes by the price of the pizza type and store it as price

'''

