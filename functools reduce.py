

import functools

d = [*range(10)]
print(d)

result = functools.reduce(lambda x,acc: acc + x, d)

print(result)
