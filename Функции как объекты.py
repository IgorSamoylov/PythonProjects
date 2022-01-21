
def yell(text):
    return text.upper() + "!"


print(yell('привет'))

# Создаем новую ссылку на объект-функцию
bark = yell

# Удаляем объект-функцию yell
del yell

print(bark('гав'))

#Отладочное имя объекта-функции в свойствах bark осталось yell
print(bark.__name__)

print(bark.__qualname__)


# Функции можно хранить в структурах данных точно так же как и любые иные объекты
funcs = [bark, str.lower, str.capitalize]
print(funcs)

for func in funcs:
    print(func('привет'))

print(funcs[0]('приветик'))


# Функции можно передавать в качестве аргументов как объект в другие функции

def greet(func):
    greeting = func('Привет! Я программа Питон')
    return greeting

print(greet(bark))
