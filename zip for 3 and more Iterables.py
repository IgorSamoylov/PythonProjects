

a = [x for x in range(10)]
b = [x for x in range(10, 20)]
c = [x for x in range(20, 25)]

z = zip(a,b,c)
for tup in z:
    print(tup)
