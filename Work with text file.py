"""
Дан файл, каждая строка которого может содержать одно или несколько целых чисел,
разделенных одним или несколькими пробелами.

Вычислите сумму чисел в каждой строке и выведите эти суммы через пробел
(для каждой строки выводится сумма чисел в этой строке).
"""

input_file = open("TEST_TEXT2.txt", "r", encoding="UTF-8")

for line in input_file:
    summa = sum(map(int, line.split())) # Встроенная функция sum Питона для iterable
    print(summa, end =' ')
