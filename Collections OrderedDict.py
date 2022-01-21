
from collections import OrderedDict

ord_dict = OrderedDict()

ord_dict[1] = "A"
ord_dict[2] = "B"
ord_dict[3] = "C"
ord_dict[4] = "D"

print("Исходный: ", ord_dict)

del(ord_dict[3])

ord_dict[3] = "C"

print("После удаления и вставки с тем же ключом ", ord_dict)
#Элемент откатывается в конец

ord_dict[2] = "F"

print("После перезаписи значения по существующему ключу ", ord_dict)
# Элемент сохраняет своё положение
