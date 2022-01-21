

#A = True
#B = False

import itertools

logic_values = itertools.product((True, False), (True, False))


for A, B in logic_values:
    print(f'A = {A} B = {B}')

    C = (not(A and B)) == ((not A) or (not B))
    print(C)

    C = (not(A or B)) == ((not A) and (not B))
    print(C)

