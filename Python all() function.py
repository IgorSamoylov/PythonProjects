# Наложение ленивой функции all на ленивый генератор кортежа приводит
# к side-effect'у ленивого исполнения по цепочке 

def is_true(n: int):
    print("Side effect!")
    return bool(n)

values = [0, 1]

print("Case 1: ")
conditions = (is_true(n) for n in values) #Ленивый генератор
print(all(conditions)) # Ленивая функция all выполняет только 1 аргумент, если он false

print("Case 2: ")
conditions = (is_true(n) for n in reversed(values)) 
print(all(conditions)) # Ленивая функция all выполняет только 2 аргумента с первым true


