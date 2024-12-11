from address import Address
from estoreproject.estore import Estore


class User(Estore):
    def __init__(self, age, email, street, state, city_name,house_number, country_name, name,password,phone):
        self.__age = age
        self.__email = email
        self.__address = Address(street, state, city_name, house_number, country_name)
        self.__name = name
        self.__password = password
        self.__phone = phone

Estore.users.append(User(3, "embrace@gmail.com", "pasuma street", "Lagos", "Lagos",3, "Nigeria", "Mark",1234,"09022345612"))

