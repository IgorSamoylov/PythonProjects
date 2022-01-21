
def test_keyword_args(intellect, force):
    print(intellect, force)

test_keyword_args(force = 10, intellect = 100) #Так мы обращаемся к именованным аргументам в функции

test_keyword_args(10, 100) #А это обычное обращение по позициям аргументов


def test_many_args(*args, **kwargs): #Сначала идут args, потом kwargs
    print(args, len(args))  # Позиционные аргументы передаются как кортеж, распаковываемый "звездочкой" на входе
    print(args[0]) # Обращение к позиционному аргументу по индексу кортежа
    print(kwargs, len(kwargs)) #Именованные аргументы передаются как словарь ключ - значение
    print(kwargs["name"]) #Обращение к именованному аргументу по строке - его названию
    kwargs["dog"] = "Senbernar"
    print(kwargs)

test_many_args(1,2,3, name = "Igor", animal = "Cat")


def default_args(inp = "Котяра"): #Так задаётся значение аргумента по умолчанию
    print(inp)

default_args()

default_args("Собака")

