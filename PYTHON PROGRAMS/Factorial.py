#! Программа по вычислению факториала
 
number = int(input("Введите число: "))
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print(f "Факториал числа {number} равен {factorial}")
factorial = str (factorial)
print(f "Число содержит {len (factorial)} разрядов") 
