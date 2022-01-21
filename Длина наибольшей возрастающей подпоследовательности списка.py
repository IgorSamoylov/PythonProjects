

def gis(a: list) -> int:
    """Возвращает длину наибольшей возрастающей подпоследовательности списка"""
    f = [0]*len(a)
    for i in range(len(a)):
        m = 0
        for j in range(i):
            if a[i] > a[j] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    return max(f) if f else 0

import random
A = [random.randint(1, 10) for x in range(1000)]

print(gis(A))
