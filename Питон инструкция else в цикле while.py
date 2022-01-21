import random

x = 0

while x < 10:
    print(x)
    if x == random.randint(0, 20): # randint генерирует случ число от арг A до B 
        break
    x += 1
else:
    print("Произошел нормальный выход без break!")
