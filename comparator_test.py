

import random
A = [(random.randint(0, 100), x) for x in range(20)]

def comparator(tup: tuple) -> int:
    return -tup[1]

A.sort(key=comparator) # Функция-компаратор передается как объект, без вызова!
print(A)

def reduce_func(akk: int, tup: tuple):
    return akk + tup[0]

import functools as ft
result = ft.reduce(reduce_func, A, 0) # В reduce функция также передается как объект, без вызова
print(result)



result = sum(map(lambda tup : tup[0], A)) # Вариант с использованием map
print(result)
    
