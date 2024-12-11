from estoreproject.user import User
from address import Address


class Seller(User):
    def __init__(self,email, age, street, state, city_name, house_number, country_name, name, password, phone):
        super().__init__(age, email, street, state, city_name, house_number, country_name, name, password, phone)
        self.email = email
        self.age = age
        self.address = Address(street, state, city_name, house_number, country_name)
        self.name = name
        self.password = password
        self.phone = phone
