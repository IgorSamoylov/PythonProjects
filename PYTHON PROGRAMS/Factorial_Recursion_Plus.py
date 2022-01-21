#! Программа по вычислению факториала
 
number = int(input("Введите число: "))

i = 0

def factorial(n):
    global i  
    i += 1
    if i == number: return n;
    return n * factorial(n + 1)  
    

print(f"Факториал числа {number} равен {factorial(1)}")
#factorial = str (factorial)
#print(f "Число содержит {len (factorial)} разрядов") 
