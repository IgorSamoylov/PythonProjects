
d = {"CAT BARSIK" : 1, "CAT PUSHOK" : 2, "CAT SNEJOK" : 3}

# Метод fromkeys создает словарь из Iterable в качестве ключей, инициализированный
# значениями None
k = {}
print(k.fromkeys("CAT BARSIK"))

# Метод setdefault добавляет значение в словарь по ключу, если оно отсуствует
# или обновляет существующее значение
d.setdefault("CAT BEGEMOT", 4)
print(d)

# Класс defaultdict() модуля collections ни чем не отличается от обычного словаря
# за исключением того, что по умолчанию всегда вызывается функция,
# которая возвращает значение по умолчанию для новых значений.
# Другими словами Класс defaultdict() представляет собой словарь
# со значениями по умолчанию.
from collections import defaultdict
dd = defaultdict(tuple)
dd["CAT BARSIK"] = (2,)
print(dd["CAT PUSHOK"])
print(dd)
