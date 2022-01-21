

A = True
B = False

# XOR - это анти-эквиваленция!
C = A != B
print(C)

# Битовый оператор ^ подходит для bool в качестве XOR, поскольку bool  -
#фактически 1 бит в int'е
C = A ^ B 
print(C)

# Прямой подход к XOR
C = (A and not B) or (not A and B)
print(C)

# Использование логической группы
С = bool(A) + bool(B) == 1
print(C)

# То же самое, что ^
from operator import xor
C = xor(bool(A), bool(B))
print(C)
