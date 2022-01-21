#Kolatz

print("Введите число")
x =  int(input())
if x <= 0:
    print("Число должно быть положительным!")  
    exit()

x_rec = x
max_number = 0
steps = 0
data_array = []

while x != 1:
    data_array.append(x)
    if x % 2 == 0:
        x = int(x / 2)
    else:
        x = x * 3 + 1

    steps += 1
    max_number = x if x > max_number else max_number
    print(f"Step {steps} x = {x}")
    

print(f"Количество шагов: {steps}, максимально достигнутое значение: {max_number}")
min_numbers = filter(lambda x : 5 < x < 100, data_array)
print(f"Минимальные значения (больше 4-х и меньше 100) ", *min_numbers)

import numpy
numpyArray = numpy.array(data_array)
import matplotlib.pyplot as mpl
fig = mpl.figure("ГИПОТЕЗА КОЛАТЦА")
mpl.title(f"График числа {x_rec}")
mpl.plot(numpyArray)
mpl.grid(True)

mpl.show()
