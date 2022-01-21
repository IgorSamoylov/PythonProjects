
gen = (x for x in range(0, 100) if x % 11 == 0)

while True:
    try:
        r = gen.__next__()
        print(r)
    except:
        break


print("Function-generator")

def gen_f():
    for x in range(0, 100):
        if x % 11 == 0:
            yield x

gen = gen_f() #Не забыть создать объект генератора

while True:
    try:
        r = gen.__next__()
        print(r)
    except:
        break
