import unittest

from book import Book


class BookTest(unittest.TestCase):

    def setUp(self):
        self.book = Book( "think well", "adam", "1200")


    def test_that_books_are_created_and_added_to_the_catologue(self):
        self.assertEqual(len(self.book.book_collection), 1)

    def test_that_books_have_their_id(self):
        book = Book( "think well", "adam", "1200")
        self.assertTrue(book._book_id)

    def testThatExceptionIsRaisedIfBookNotFound(self):
        self.assertRaises(ValueError, self.book.search_book, "thinkwell")
