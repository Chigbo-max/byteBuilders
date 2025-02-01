from payment import Payment
from shoppingcart import ShoppingCart
from order import Order
from book import Book
from user import User
import random

class Customer(User):

    customers = []

    def __init__(self, first_name, last_name, email:str):
        super().__init__(first_name, last_name, email)
        self.__id = self.generate_customer_id()
        self.customers.append(self)
        self.shopping_cart = ShoppingCart()
        self.orders = []


    def generate_customer_id(self):
        return 'CK' + str(random.randint(100000, 999999))

    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.__id == customer_id:
                return customer
            else:
                raise Exception('ID not found')

    @property
    def __id(self):
        return self._id

    @__id.setter
    def __id(self, value):
        self._id = value



    def browse_books(self):
        for book in Book.book_collection:
            print(f"""
            Book ID: {book._book_id}
            Title: {book._title}
            Author: {book._author}
            Price: NGN{book._price}
            """)

    def search_books(self, title: str):
        for book in Book.book_collection:
            if book.__title.lower() == title.lower():
                return f"Book Found: Title: {book.__title}, Author: {book.__author}, Price: NGN{book.__price}"
        return f"No book found with title: {title}"


    def find_book_by_id(self, book_id):
        for book in Book.book_collection:
            if book._book_id == book_id:
                return book
        raise ValueError("Book not found")

    def add_to_cart(self, book_id):
        book = self.find_book_by_id(book_id)
        self.shopping_cart.add_cart(book._book_id, quantity=1)

    def remove_books_from_cart(self, book_id):
        for book in self.shopping_cart.get_items():
            if book[0] == book_id:
                self.shopping_cart.remove_from_cart(book_id)
            else:
                raise Exception("Book not found")


    def view_cart(self):
        items = self.shopping_cart.get_items()

        if not items:
            raise ValueError("No items found")

        for item in items:
            book_id, quantity = item
            book = self.find_book_by_id(book_id)
            price = book._price * quantity

            return f"""
                BOOK ID: {book_id}
                QUANTITY: {quantity}
                PRICE: {price}
                """
        return items


    def place_order(self, book_id, quantity):
        if not self.shopping_cart.get_items():
            raise ValueError("Shopping cart is empty, please add book first")
        order = Order(book_id, quantity)
        self.orders.append(order)
        return order


    def make_payment(self,order, amount):
        if not self.orders:
            raise Exception("No order made yet")
        payment = Payment(order, amount)
        return payment.pay()

    def get_orders(self):
        return self.orders


    def view_order_history(self):
        if not self.orders:
            raise Exception("No order made yet")
        return "\n".join([str(order) for order in self.orders])

    def __str__(self):
        return f"""
            LOGIN-ID: {self.__id}
        """


