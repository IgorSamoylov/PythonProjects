
import collections

x = [1, 2, 3, 1, 1, 4, 5, 6, 7, 6, 8]
result_counter = collections.Counter(x)
print(result_counter)

# Возвращает list кортежей созданных из словаря и сохраняющий исходный порядок,
# по возможности. Другими словами объект - список кортежей ключ-значение, имеющи1
# свойства словаря
ordered_dict = collections.OrderedDict(result_counter)
print(ordered_dict)

# Создаёт представление посредством объединения нескольких исходных словарей,
# позволяющее обновлять входящие элементы
chain_map = collections.ChainMap({1 : "bars", 2 : "cat"}, dict([(3,"tiger"), (4, "dog")]))
print(chain_map)
