'''
PSEUDO CODE
1. create function  called my_discount
2. let the function take two parameters, price and discount
3. let the discount be divided by 100 and stored as constant DISCOUNT
4. multiply DISCOUNT by price and subtract the value from the price, store as new_price
4. return the price after the discount
'''

def my_discount(price, discount):
	
	if(price < 0 or discount < 0):
		raise ValueError("Invalid number")

	DISCOUNT = discount / 100
	
	new_price = price - (DISCOUNT * price)

	return new_price