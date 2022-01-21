
def one():
    print("One!")

def two():
    print("Two!")

def three():
    print("Three!")

dictWithFun = {1 : one, 2 : two, 3 : three}

# Прямой вызов функции по ключу - посредством ()
dictWithFun[1]()

# Первый способ итерации по словарю
for number in dictWithFun:
    print("Запускаю ", number)
    dictWithFun[number]()

# Второй способ - с использованием метода dict.items(), возвращающего кортежи ключ-значение
for kv_tuple in dictWithFun.items():
    print("Запускаю ", kv_tuple[0])
    kv_tuple[1]()

# То же самое, с указанием самого кортежа в заголовке for
for key, value in dictWithFun.items():
    print("Запускаю ", key)
    value()

# Итерация по ключам словаря, возвращенным функцией dict.keys()
for key in dictWithFun.keys():
    print("Запускаю ", key)
    dictWithFun[key]()

# Итерация по значениям словаря, возвращенным функцией dict.values()
for value in dictWithFun.values():
    value()
    
