"""
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO, если не встречалось.

Для примера:
Ввод 	Результат

1 2 3 2 3 4

NO
NO
NO
YES
YES
NO
"""



inp_list = list(map(int, input().split()))

inp_set = set()

for i in inp_list:
    
    if(i in inp_set): 
        print("YES")
    else: 
        print("NO")
        inp_set.add(i)
