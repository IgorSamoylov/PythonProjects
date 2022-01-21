
from collections import OrderedDict
import random

od = OrderedDict()

basic_dict = {x : random.randint(1, 10) for x in range(1, 101)}

od.update(basic_dict)

print(od)
