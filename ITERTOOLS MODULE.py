import itertools

list1 = ['A','B','C','D','E','F']
list2 = [1, 2, 3, 4, 5, 6]

#Комбинационные итераторы

#Эквивалент вложенных циклов перебора нескольких Iterable
print("ITERTOOLS PRODUCT")
print(*itertools.product(list1, list2, repeat=1))

#Перебор всех вариантов сочетаний элементов одного Iterable с заданной длиной результата
print("ITERTOOLS PERMUTATIONS")
print(*itertools.permutations(list1, 2))

#Перебор результатов, включающих оба элемента, независимо от последовательности (меньше, чем permutation)
print("ITERTOOLS COMBINATION")
print(*itertools.combinations(list1, 2))

#Сложение первого со следующим элементов. Аналог reduce
print("ITERTOOLS ACCUMULATE")
print(*itertools.accumulate(list2)) # По умолчанию идёт сложение элементов Iterable
print(*itertools.accumulate(list2, lambda x, y: x + y + 1000))



#Бесконечные итераторы:

#Последовательно перебирает переданные Iterable
print("ITERTOOLS CHAIN")
print(*itertools.chain(list1, list2, list1))

#Бесконечно перебирает элементы Iterable
print("ITERTOOLS CYCLE")
iterator_cycle = itertools.cycle(list1)
for i in range(20):
    print(iterator_cycle.__next__(), end=' ')
print('\n')


#Генератор бесконечной последовательности int чисел, начиная с первого, с нужным шагом
print("ITERTOOLS COUNT")
iterator_count = itertools.count(100,2)
for i in range(20):
    print(iterator_count.__next__(), end=' ')
print('\n')


#Включает и выключает элементы первого Iterable в зависимости от логических значений второго
print("ITERTOOLS COMPRESS")
print(*itertools.compress(list1, [0,1,0,1,0,1]))

#Возвращает кортеж независимых итераторов в количестве n на один переданный Iterable
print("ITERTOOLS TEE")
tee_tuple = itertools.tee(list1, 3)
print(*tee_tuple[0], *tee_tuple[1])

#Возвращает словарь, образованный на основе анализа Iterable, переданного первым аргументом
#функцией группировки (функция возвращает ключ, соответствующий нескольким элементам из Iterable)
#значением словаря является кортеж из всех элементов, соответсвующих ключу
print("ITERTOOLS GROUPBY")
data_string = 'AAAAFFFFGGTYHHHHHUUI'

def grouper(string):
    return ord(string) # ord возвращает int значение для unicod-символа

data_string = sorted(data_string, key=grouper)
# Возвращает кортеж из ключа группировки и нескольких итераторов на соотв. элементы в iterable
for key, group in itertools.groupby(data_string, grouper):
    print(f"KEY: {key}")
    for item in group:
        print(f"ITEM: {item}")

