class ShoppingCart:

    def __init__(self):
        self._items = []


    def get_items(self):
        return self._items


    def add_cart(self, book_id, quantity=1):
        self._items.append((book_id, quantity))

    def clear_cart(self):
        self._items = []

    def remove_from_cart(self, book_id):
        for book in self._items:
            if book[0] == book_id:
                self._items.remove(book)
            else:
                raise Exception("Book not found")

    def view_shopping_cart(self):
        return "\n".join([str(item) for item in self._items])

    def __str__(self):
        return f"""
        items: {self._items}
        """



