import random

class Book:
    book_collection = []

    def __init__(self, title, author, price: float):
        self.__book_id = self.generate_book_id()
        self.__title = title
        self.__author = author
        self.__price = price
        self.book_collection.append(self)

    @property
    def __book_id(self):
        return self._book_id

    @__book_id.setter
    def __book_id(self, value):
        self._book_id = value

    @property
    def __title(self):
        return self._title

    @__title.setter
    def __title(self, value):
        self._title = value

    @property
    def __author(self):
        return self._author

    @__author.setter
    def __author(self, value):
        self._author = value


    @property
    def __price(self)->float:
        return self._price

    @__price.setter
    def __price(self, value: float):
        self._price = value


    def generate_book_id(self):
        return 'BK' + str(random.randint(100000, 999999))




    def __str__(self):
        return f"""
        Book ID: {self.__book_id}
        Book Title: {self.__title}
        Book Author: {self.__author}
        Price: {self.__price}
        """

book1 = Book("think well", "adam", 1200)
book2 = Book("dream well", "adam", 1200)
book3 = Book("talk well", "adam", 1200)


