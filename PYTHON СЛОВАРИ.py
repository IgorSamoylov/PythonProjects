
f = {1 : "cat", 2 : "dog", 3 : "bear"} #Обычная инициализация словаря {key1 : value, key2 : value}

print(f[1])

d = dict(short='dict', long='dictionary', main='словарь') #Создание словаря функцией dict и присваиванием

print(d)

k = dict([(1, 1), (2, 4), (3, "котяра"), (4, "собака")])# Создание словаря функцией dict из массива кортежей

print(k)

k[3] = "Наглый котяра!" #Замена значения по ключу

print(k)

l = dict.fromkeys([1,2,3], "bear") #Создание словаря dict.fromkeys с одним значением для всех

print(l[3])

n = {a: a**2 for a in range(10)} #Создание словаря генератором словарей

print(n)

#Создание словаря из двух списков методами dict и zip
keys = (a for a in range(20))
values = [a*2 for a in range(20)]
p1 = dict(zip(keys, values))
print(p1)

#Тестируем время выполнения лямбды с созданием словаря через zip
import timeit
print(min(timeit.repeat(lambda: dict(zip(keys, values)))))

import numpy
list1 = (numpy.random.random(100))
list2 = (numpy.random.random(100))

#print(min(timeit.repeat(lambda: dict(zip(list1, list2)))))

dict777 = dict(zip(list1, list2))
print(dict777.items())







