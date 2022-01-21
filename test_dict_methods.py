
import random
D = {x : int(random.triangular(0, 100.0, 20.0)) for x in range(10)}

result = D.get(1)
print(result)

result = D.pop(1)
print(result)

result = D.setdefault(2, 777)
print("Устанавливаем  и возвращаем значение, если нет ключа", result)
print(D)

result = D.popitem()
print("Удаляем и возвращаем 1 случайный кортеж", result)
print(D)

print(D.keys(), D.values(), D.items(), sep='\n')
