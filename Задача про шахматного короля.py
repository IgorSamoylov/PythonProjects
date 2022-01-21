

n = 8 # элементы в строке (колонки)
m = 8 # строки

path_num = [[0] * (n + 1) for i in range(m + 1)]
path_num[0][1] = 1 # позволит не делать в циклах исключения для стартовой клетки
for i in range (1, m + 1):
    for j in range (1, n + 1):
        path_num[i][j] = path_num[i][j - 1] + path_num[i - 1][j]
print(path_num[-1][-1])
