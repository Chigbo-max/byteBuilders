from user import User
from address import Address

class Customer(User):
    def __init__(self, age, email, street, state, city_name, house_number, country_name, name, password, phone):
        super().__init__(age, email, street, state, city_name, house_number, country_name, name, password, phone)
        self.age = age
        self.email = email
        self.address = Address(street, state, city_name, house_number, country_name)
        self.name = name
        self.password = password
        self.phone = phone

