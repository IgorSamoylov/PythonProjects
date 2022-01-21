setFromMap = set(map(abs, [2, -4, 7, -8]))
print("setFromMap:", setFromMap)
#Создание множества функцией set из map, применяющей функцию abs, переданную первым аргументом
#к итерируемой последовательности

setFromRange = set(range(-10, 10, 2))
print("setFromRange:", setFromRange)

setFromTuple = set((1,1,2,2,3,3,3))
print("setFromTuple: ", setFromTuple)

my_set = {1, 2, 3, 4, 3} #Множество уничтожает повторные значения с одинаковым хешом
print(my_set)

my_set.add(777) #Добавление элемента функцией .add Так же как в JAVA!
my_set.discard(3) #Удаление без ошибки
my_set.remove(1) #Удаление с ошибкой при отсутствии элемента. Как в JAVA

print(my_set)
if 777 in my_set: #Проверка наличия элемента
    print(my_set)


my_set |= setFromTuple #Объединение множеств set.update()
my_set -= setFromRange  #Вычитание множества set.difference_update()
my_set ^= setFromMap #Элементы из объединения множеств, не входящие в их пересечение. Исключающее ИЛИ
# set.symmetric_difference_update()
my_set &= setFromTuple #Пересечение множеств (и там и там) set.intersection_update()



print("Пересечение: ", my_set)

my_set.clear() # Очистка множества


FrozenSet = frozenset([1,1,7,7,9,9,0,0])#Неизменяемое множество
print(sorted(FrozenSet)) #Функция sorted
