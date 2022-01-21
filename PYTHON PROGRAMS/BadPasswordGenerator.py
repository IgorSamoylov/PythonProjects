import random

class BadPasswordGenerator:
    """
    Генератор небезопасных паролей
    """
    def __init__(self):
        self.i = 0
        with open ('10000passwords.txt') as f :
           passwords_data = f.read ()
        self.passwords = passwords_data.split('\n') 

    def next(self):
        password = self.passwords[self.i]
        self.i += 1
        return password


generator = BadPasswordGenerator()

i = 0
while i < 1000:
    print(generator.next())
    i += 1









