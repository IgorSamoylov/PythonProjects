#! Программа по вычислению факториала
 
number = int(input("Введите число: "))
i = 1
#factorial = 1

def factorial(n):
    if n == 1: return 1;
    return n * factorial(n - 1)  
    
#factor = factorial(number)
print(f"Факториал числа {number} равен {factorial(number)}")
#factorial = str (factorial)
#print(f "Число содержит {len (factorial)} разрядов") 
