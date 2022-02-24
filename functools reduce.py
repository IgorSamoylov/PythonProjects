

import functools

d = [*range(10)]

#result = functools.reduce(lambda x,acc: acc + x, d)
result = functools.reduce(lambda x,y: x + y, d)

print(result)
