

from functools import lru_cache


@lru_cache(maxsize=30)
def fibon_calculate(n: int):

# Здесь затратная операция, выбирающая статьи
# на определённую дату.
    fibon = lambda n: fibon(n-2) + fibon(n-1) if n > 2 else 1 
    return fibon(n)


print(fibon_calculate(10))
print(fibon_calculate(20))
print(fibon_calculate(10))  # Взяты из кеша.


# Рассмотрим эффективность кеша:
print(fibon_calculate.cache_info())
