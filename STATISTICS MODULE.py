import random
import statistics

x = [random.randint(1, 100) for x in range(30)]
print(x, sep="     ", end="\n")

# ******* ВЫЧИСЛЕНИЕ СРЕДНИХ ЗНАЧЕНИЙ *******

result = statistics.mean(x)
print("СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ ", result)

result = statistics.fmean(x)
print("СРЕДНЕЕ С ПЛАВАЮЩЕЙ ТОЧКОЙ ", result)

result = statistics.geometric_mean(x)
print("СРЕДНЕЕ ГЕОМЕТРИЧЕСКОЕ ", result)

result = statistics.harmonic_mean(x)
print("СРЕДНЕЕ ГАРМОНИЧЕСКОЕ ", result)

result = statistics.median(x), statistics.median_low(x), statistics.median_high(x)
print("МЕДИАНА АБСТРАКТНАЯ, НИЖНЯЯ, ВЕРХНЯЯ ", result)


# ОПРЕДЕЛЕНИЕ НАИБОЛЕЕ ЧАСТО ВСТРЕЧАЮЩЕГОСЯ ЗНАЧЕНИЯ (most common value)
result = statistics.mode(x)
print("НАИБОЛЕЕ ЧАСТО ВСТРЕЧАЮЩЕЕСЯ ",  result)


# ******* Calculating variability or spread *******

result = statistics.pvariance(x)
print("POPULATION VARIANCE ", result)

result = statistics.variance(x)
print("SAMPLE VARIANCE ", result)

result = statistics.pstdev(x)
print("POPULATION STANDARD DEVIATION ", result)

result = statistics.stdev(x)
print("SAMPLE STANDARD DEVIATION ", result)
