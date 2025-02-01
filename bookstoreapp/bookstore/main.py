
from customer import Customer


class Main:


    def display_main_menu(self):
        self.go_to_menu()

    def __init__(self):
        self.customer = None
        self.order = None

    def go_to_menu(self):
        menu = '''
        WELCOME TO ONWARD ONLINE BOOKSTORE
        1 -> Register
        2 -> Login
        3 -> Logout
        '''
        print(menu)
        self.input_menu()

    def input_menu(self):
        try:
            choice = input("Select a number if you would like to register or login to logout?")
            match(choice[0]):
                case '1':
                    self.register()
                case '2':
                    self.login()
                case '3':
                    self.log_out()
                case _:
                    print("Invalid input try again")
                    self.go_to_menu()
        except ValueError:
            print("Invalid input try again")




    def register(self):

        if self.customer is not None:
            print("Please proceed to login as you are already registered")
            self.go_to_menu()
        else:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            self.customer = Customer(first_name, last_name, email)
            print("Registration successful")
            print(f"{self.customer.__str__()}")
            print("Please proceed to login")
            self.go_to_menu()

    def login(self):
        if self.customer is None:
            print("Please register first")
            self.go_to_menu()
        else:
            customer_id = input("Enter your ID: ")
            self.customer.find_customer_by_id(customer_id)
            print("log in successful")
            self.access_dashboard()


    def log_out(self):
        print("Thanks for using our App")


    def access_dashboard(self):
        dashboard = '''
        WELCOME TO ONWARD ONLINE BOOKSTORE
        1 -> Browse books
        2 -> Search books
        3 -> Add to cart
        4 -> Remove from cart
        5 -> View shopping cart
        6 -> Place an order
        7 -> Make payment
        8 -> View order history
        9 -> Log out
        '''
        print(dashboard)
        self.input_dashboard()

    def input_dashboard(self):
        try:
            choice = input("Enter your choice: ")
            match(choice[0]):
                case '1':
                    self.browse_books()
                case '2':
                    self.search_books()
                case '3':
                    self.add_to_cart()
                case '4':
                    self.remove_from_cart()
                case '5':
                    self.view_cart()
                case '6':
                    self.place_an_order()
                case '7':
                    self.make_payment()
                case '8':
                    self.view_order()
                case '9':
                    self.log_out()
                case _:
                    print("Invalid input try again")
                    self.go_to_menu()
        except ValueError as e:
            print(f"{e}")
        finally:
            self.access_dashboard()

    def browse_books(self):
        self.customer.browse_books()
        self.access_dashboard()

    def search_books(self):
            book_title = input("Enter the book title (please copy and paste from the book list): ")
            print(self.customer.search_books(book_title))
            self.access_dashboard()

    def add_to_cart(self):
        book_id = input("Enter the book id: ")
        self.customer.add_to_cart(book_id.strip())
        print(f"Book with ID:{book_id} Added to cart succesfully")
        self.access_dashboard()

    def remove_from_cart(self):
        try:
            book_id = input("Enter the book id: ")
            self.customer.remove_books_from_cart(book_id.strip())
            print(f"Book with ID:{book_id} removed from cart succesfully")
            self.access_dashboard()
        except Exception as e:
            print(f"{e}")

    def view_cart(self):
        try:
            print(self.customer.view_cart())
            self.access_dashboard()
        except ValueError as e:
            print(f"{e}")


    def place_an_order(self):
        book_id = input("Enter the book id: ")
        quantity = input("Enter the quantity: ")
        self.order = self.customer.place_order(book_id, quantity)
        print(f"Book with ID:{book_id} placed successfully")
        self.access_dashboard()

    def make_payment(self):
        try:
            amount = input("Enter the amount: ")
            print(self.customer.make_payment(self.order,float(amount)))
            self.access_dashboard()
        except Exception as e:
            print(f"{e}")


    def view_order(self):
        try:
            print(self.customer.view_order_history())
            self.access_dashboard()
        except Exception as e:
            print(f"{e}")


Main().display_main_menu()

