

set1 = set((1,2,3,4))
set2 = set((2,3))

set3 = set1 ^ set2 # Исключающее ИЛИ, intersection

print(set3)

set3 = set1 | set2

print(set3) # Обычное ИЛИ, union

set3 = set1 - set2 # Разность, difference

print(set3)

set1.update(set2) # Дополнить первое множество элементами второго 

print(set1)


list1 = [1,2,3,4] # А для списков используется функция extend!
list2 = [2,3]
list1.extend(list2)
print(list1)
