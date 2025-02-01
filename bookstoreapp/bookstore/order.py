from book import Book
from shoppingcart import ShoppingCart

class Order:
    order_history = []

    def __init__(self, book_id, quantity):
        self.book_id = book_id
        self.quantity = quantity
        self.total_price = float(0)
        self.calculate_total_price()
        self.order_history.append(self)


    def calculate_total_price(self):
        for book in Book.book_collection:
            if self.book_id == book._book_id:
                self.total_price = float(book._price) * float(self.quantity)
                return
        raise ValueError("Book ID not found")


    @property
    def get_total_price(self)-> float:
        return self.total_price

    @get_total_price.setter
    def get_total_price(self, value):
        self.total_price = value

    def get_order_history(self):
        return self.order_history

    def __str__(self):
        return(
            f"""
            Book ID: {self.book_id} 
            Quantity: {self.quantity} 
            Total price: NGN{self.total_price}
            """
        )
