
"""
Выбрасывание яиц из здания. Пусть имеется N-этажное здание и много яиц.
Пусть также яйцо разбивается, если оно выбрасывается с этажа F или выше.
Вначале разработайте стратегию для определения значения F, разбив ~lgN яиц
и выбросив ~lgN раз, а затем найдите способ снизить стоимость до ~2lgF.
"""

N = 1100
F = 900

count = 0
def check_smashing(level: int) -> bool:
    global count
    count += 1
    print("Проверяем на ", level, " этаже, попытка номер ", count)
    return F <= level <= N
    

def binary_search(low: int, hi: int):
    while low <= hi:
        mid = (hi - low) // 2 + low
        print(low, mid, hi)
        if check_smashing(mid):
            hi = mid - 1
        else:
            low = mid + 1
    return hi
    

def search_level() -> int:
    """ Проверяет все этажи снизу вверх с увеличивающимся x2 шагом,
        запоминет последнюю успешную попытку и вызывает binary_search
        для поиска в даипазоне разбивается - не разбивается"""
    last_i = 0
    i = 1
    while i <= N:
        if check_smashing(i):
            return binary_search(last_i+1, i-1)
        last_i = i
        i *= 2
    return binary_search(last_i+1, N)

print("Яйцо не разобъется при падении с: ", search_level(), " этажа")
