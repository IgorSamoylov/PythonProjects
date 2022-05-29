"""В стандартной библиотеке C++ есть функция std::next_permutation.
Она по перестановке в массиве строит следующую в лексикографическом порядке.
Время построения в среднем константное, дополнительная память тоже константная.
Повторяющиеся элементы обрабатываются автоматически.
Генератор перестановок ниже основан на этой функции:
"""

import sys


def next_permutation(a):

    def swap(i, j):
        a[i], a[j] = a[j], a[i]

    def reverse_tail(i):
        j = len(a) - 1
        while i < j:
            swap(i, j)
            i += 1
            j -= 1

    if len(a) <= 1:
        return False

    i = len(a) - 1
 
    while True:
        i1 = i
        i -= 1
        if a[i] < a[i1]:
            i2 = len(a)
            while True:
                i2 -= 1
                if a[i] < a[i2]:
                    break
            swap(i, i2)
            reverse_tail(i1)
            return True

        if i == 0:
            reverse_tail(0)
            return False


def permutations(a):
    a = sorted(list(a))
    yield a
    while next_permutation(a):
        yield a


for p in permutations(map(int, sys.argv[1:])):
    print(p)
