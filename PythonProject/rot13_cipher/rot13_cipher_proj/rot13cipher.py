def array_to_string(array):
    string = ""
    return string.join(array)

def encrypt_text(text):

    texts = []
    num = 13
    for i in text:
        character = chr(num + ord(i) )
        texts.append(character)
    return array_to_string(texts)





#allows u to work with files easily e.g a java file... files act as external storage because u can always go back to them
#w for write, r for read, r+ for read and write
# the first argument is the name or the path to the file
# file = open('data.txt','w')
# file.write("Jesse is a boy \n ")
# file.write("Jesse is a boy \n ")
# file.write("Jesse is a boy \n ")
#make sure u close an resorce u are working with else it corrupts the bits or use.... with open('data.txt', 'w') as file: (to close--- this is the best method)
# file.close()
#
# class User:
#     def __init__(self,name,password):
#         self.name = name
#         self.password = password
#
#
# def main():
#     name = input("Enter your name: ")
#     password = input("Enter your password: ")
#     user = User(name,password)
#
#     with open('data.txt','w') as file:
#         file.write(f'{user.name} {user.password}\n')

# class invalidPhoneException(Exception):
#     def __init__(self, message):
#         super().__init__(message)

        #mode='r' is a keyword argument
# try:
#     with open('data.txt', mode='r') as read_file:
#         data = read_file.read()
#         print(data)
# except FileNotFoundError  as e:
#     print("file not found", e)

#
# main()

# replace if statements for polymorphism, xl4j, logging module

from abc import ABC, abstractmethod

#you can't make an instance of the logger class when it hs been made abstact
#polymorphism, interface
class Logger(ABC):
    @abstractmethod
    def log(self, level,message):
        pass

class ConsoleLogger(Logger):
    def log(self,level, message):
        print(f'Logging to the console -> {level}{message}')

class FileLogger(Logger):
    def log(self, level, message):
        with open('file.txt', 'w') as file:
            file.write(f'Logging to the file -> {level}{message}')








