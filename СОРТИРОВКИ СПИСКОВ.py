
def insertion_sort(A):
    """ сортировка списка А вставками """
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k - 1] > A[k]: # Поскольку and ленивое, то при k = 0 второе выражение k - 1 не будет выполняться и мы не получим ошибки выхода за границы списка
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1

def selection_sort(A):
    """ сортировка списка А выбором """
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[pos] > A[k]:
                A[pos], A[k] = A[k], A[pos]

def bubble_sort(A):
    """ сортировка списка А методом пузырька """
    N = len(A)
    for traverse in range(1, N):
        for k in range(0, N - traverse):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]

import random
array = [random.randint(0,100) for x in range(10)]
print(array)
#insertion_sort(array)
selection_sort(array)
#bubble_sort(array)
print(array)
