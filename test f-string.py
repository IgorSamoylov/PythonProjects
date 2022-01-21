
n = 100
string1 = f"{n} - это сто"
print(string1)

# Вариант 1, пустые фигурные скобочки
string2 = "{} - это сто".format(n)
print(string2)

# Вариант 2, с указанием имени переменной
string2 = "{n} - это сто".format(n=n)
print(string2)

# Old style
# %x конвертирует в 16-ричную систему
string3 = " %x - это %p " % (n, n) #  % справа принимает только 1 аргумент, т.е. должен быть кортеж
print(string3)
