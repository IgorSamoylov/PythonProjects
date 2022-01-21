

list2D = [[0] * 10 for m in range(10)]

print(list2D)

DIMENSION = 10
list2D = [[m * n for m in range(1, DIMENSION)] for n in range(1, DIMENSION)]

for n_line in list2D:
    for m_line in n_line:
        print(m_line, end=' ')
    print('\n')


list2D2 = [[1, 2], [3, 4], [5, 6]]
print(list2D2)

# Неправильный путь
m = 5; n = 5
a = [[0] * m] * n
print(a)
a[0][1] = 2
print(a)