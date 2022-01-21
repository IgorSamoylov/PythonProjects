# print (passwords [ :10])                                       #Слайс, диапазон через двоеточие, первый элемент берется включительно, последний - исключительно


# Смысл класса в отличие от простой функции, что он
# хранит своё состояние в своих переменных - атрибутах

class BadPasswordGenerator:
    """
    Генератор небезопасных паролей
    """

    def __init__(self):
        self.i = 0
        self.passwords = passwords_data.split(
            '\n')  # Функция split делит строку по символу переноса строки и возвращает list из отдельных строк

    def next(self):
        password = self.passwords[self.i]
        self.i += 1
        return password


generator = BadPasswordGenerator()

print(generator.next())
print(generator.next())

# with open ('passwords.txt') as f :
#   passwords_data = f.read ()


import random


class GoodPasswordGenerator:
    """
    Генератор безопасных паролей
    """

    def __init__(self):
        # """Инициализация генератора"""
        self.alphabet = '1234567890' \
                        'qwertyuiopasdfghjklzxcvbnm' \
                        'QWERTYUIOPASDFGHJKLZXCVBNM' \
                        '!@#$%^&*()_+'

    def next(self, length=10):  # Параметр по умолчанию функции применяется, если не будет передан аргументоа
        #  """Получение следующего пароля"""
        password = ''
        for i in range(length):
            c = random.choice(self.alphabet)  # Функция choice выбирает один элемент из итерируемого объекта
            password += c

        return password


generator2 = GoodPasswordGenerator()
print(generator2.next())
print(generator2.next())

