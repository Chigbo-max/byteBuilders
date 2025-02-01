class User:
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email


    @property
    def __full_name(self):
        return f"{self._first_name} {self._last_name}"

    @__full_name.setter
    def __full_name(self, value):
        self._first_name = value
        self._last_name = value

    @property
    def __email(self):
        return f"{self._email}"

    @__email.setter
    def __email(self, value):
        self._email = value
