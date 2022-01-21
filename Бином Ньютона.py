import math as m


def binom_koef(n, k) -> int:
    return int(m.factorial(n) / (m.factorial(k) * m.factorial(n - k)))
    

while True:
    print('Введите количество элементов массива')
    n = int(input())

    print('Введите размер требуемой группы')
    k = int(input())
  
    print(f'Количество возможных комбинаций,\
          включающих все {k} элемента: ', binom_koef(n, k))
    
