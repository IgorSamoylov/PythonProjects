

my_dict = {1 : 'Barsik', 2 : 'Snejok', 3 : 'Pushok'}

print(my_dict.values()) # Метод .values() возвращает Iterable объект класса dict_values
print(my_dict.keys()) # Метод .keys() возвращает Iterable объект класса dict_keys
print(my_dict.items()) # Метод .items() возвращает Iterable объект класса dict_items, содержащий кортежи (ключ, значение)


my_dict2 = my_dict.copy()

try:
    while(True):
        print(my_dict.popitem())
except:
    pass

my_dict_iterator = iter(my_dict2)

try:
    while(1):
        iter_value = my_dict_iterator.__next__() # Объект-итератор для dict возвращает ключ на каждый вызов __next__()
        print(iter_value, my_dict2[iter_value])
except:
    pass
