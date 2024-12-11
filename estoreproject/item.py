from estoreproject.shoppingcart import ShoppingCart
from product import Product





class Item:
    def __init__(self, quantity, product_id, product_name, price, product_description):
        self.quantity = quantity
        self.product = Product(product_id, product_name, price, product_description)

ShoppingCart.items.append(Item(1, '001', ' Nike90', 500, "in stock" ))