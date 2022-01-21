"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

Для каждого из запроса выведите название страны, в котором находится данный город.

Для примера:
Ввод 	Результат

2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Odessa
3
Odessa
Moscow
Novgorod

	

Ukraine
Russia
Russia
"""



number = int(input())

dict1 = {}
for i in range(number):
    inp_str = input()
    inp_list = inp_str.split()
    country = inp_list.pop(0)
    for city in inp_list:
        dict1[city] = country

count = int(input())
query_list = []
for i in range(count):
    query_list.append(input())

for query in query_list:
    print(dict1[query])
