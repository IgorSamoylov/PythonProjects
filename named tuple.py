
from collections import namedtuple

# Позволяет задать в кортеже имена элементов в строке через пробел вторым параметром
Point = namedtuple("Pnt", "x y z") 
A = Point(100, 11, 21) # Работа как с обычным кортежем

dist_to_zero = (A.x ** 2 + A.y ** 2 + A.z ** 2) ** 0.5
print(dist_to_zero)
