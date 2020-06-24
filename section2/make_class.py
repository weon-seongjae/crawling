# Classes Documentation : https://docs.python.org/3/tutorial/classes.html

import sys
import io


class User_info():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print('-' * 30)
        print('Name: ' + self.name)
        print('Phone: ' + self.phone)
        print('-' * 30)

    def __del__(self):
        print('delete!')


user1 = User_info('kim','010-3433-7777')
user2 = User_info('park', '010-7777-7777')

print(id(user1))
print(id(user2))

# user1.set_info('kim','010-3433-7777')
# user2.set_info('park', '010-7777-7777')

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)




