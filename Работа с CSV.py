
with open("values.csv", "r", encoding="utf8") as file:
    csv = file.read()

import re
pattern = re.compile('[;\n]')  # Компилируем regex в паттерн командой re.compile(r'regex')
values = re.split(pattern, csv) # Так работает split в библиотеке re, возвращает нарезанный list

print(values)
