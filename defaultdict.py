
from collections import defaultdict # Находится в модуле collections

def default_value():
    return 1

dd = defaultdict(default_value) # В конструктор объекта defaultdict передается тип дефолтного value

result = dd["A"] # Пытаемся получить несуществующий элемент по ключу "A"

print(result) # Это не вызывает ошибки, result принимает дефолтное для типа int значение 0

print(dd) # Печаетаем новое содержимое объекта defaultdict

