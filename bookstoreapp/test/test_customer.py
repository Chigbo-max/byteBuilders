import unittest
from encodings.punycode import selective_find

from book import Book
from customer import Customer
from shoppingcart import ShoppingCart
from order import Order


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.book = Book("think well", "adam", "1200")
        self.customer = Customer("wale", "wale", "wale@gmail.com")
        self.shoppingcart = ShoppingCart()


    def testThatSearchReturnsTheBookTitle(self):
        self.assertEqual(self.customer.search_books("think well"), self.book._title)

    def testThatExceptionIsRaisedIfBookNotFound(self):
        self.assertRaises(ValueError, self.customer.search_books, "well")


    def testThatCustomerCanAddToCart(self):
        self.customer.add_to_cart(self.book._book_id)
        self.assertEqual(len(self.customer.shopping_cart.get_items()), 1)

    def testThatCustomerCanRemoveFromCart(self):
        self.customer.add_to_cart(self.book._book_id)
        self.customer.add_to_cart(self.book._book_id)
        self.customer.remove_books_from_cart(self.book._book_id)
        self.assertEqual(len(self.customer.shopping_cart.get_items()), 1)

    def test_that_exception_is_raised_when_customer_makes_an_empty_order(self):
        self.assertRaises(ValueError, self.customer.place_order, 23,4)

    def test_that_customer_can_place_an_order(self):
        self.customer.place_order(self.book._book_id,4)
        self.assertEqual(len(self.customer.get_orders()), 1)


    def test_that_error_is_raised_when_customer_has_an_empty_cart_but_wants_to_pay(self):
        order = Order(self.book._book_id, "0")
        self.assertRaises(ValueError, self.customer.make_payment, order)

    def test_that_payment_is_successful(self):
        self.customer.add_to_cart(self.book._book_id)
        self.customer.place_order(self.book._book_id,4)
        order = Order(self.book._book_id, "4")
        self.assertTrue(self.customer.make_payment(order, 1000))










