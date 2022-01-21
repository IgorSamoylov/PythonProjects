import statistics as stat

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data)

res = stat.mean(data) # Среднее арифметическое простое
print("mean ", res)

res = stat.fmean(data) # Конвертирует во float и считает среднее арифметическое
print("fmean, float mean ", res)

res = stat.geometric_mean(data) # Среднее геометрическое (произведение(product) всех чисел)
print("geometric_mean ", res)

# Harmonic mean of three values a, b and c will be equivalent to 3/(1/a + 1/b + 1/c)
res = stat.harmonic_mean(data)
print("harmoinc_mean ", res)

# Промежуточное среднее значение во всей последовательности
res = stat.median(data)
print("median ", res)

# Число - член последовательности, нижнее по отношению к общему среднему числу
res = stat.median_low(data)
print("median_low ", res)

# Число - член последовательности, верхнее по отношению к общему среднему числу
res = stat.median_high(data)
print("median_high ", res)

# Median of grouped continuous data, calculated as the 50th percentile, using interpolation.
res = stat.median_grouped(data, interval=2)
print("median_grouped ", res)

#Числа типа Decimal
from decimal import Decimal as D
print(stat.mean([D("0.5E+89"), D("0.75"), D("0.625"), D("0.375")]))

# Класс дробей!
from fractions import Fraction as F
print(stat.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))

