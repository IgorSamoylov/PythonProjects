

def test(n):
    if n == 0:
        print('Достигнут конец рекурсии!') # На допустимую  глубину рекурсии влияет размер ф-ии
        return
    test(n - 1)


for i in range(1200, 1000, -1):
    try:
        test(i)
    except:
        print(f'{i} - ошибка')
    else:
        print(f'{i} - нормальное выполнение')
        break
    
