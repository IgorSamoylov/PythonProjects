

gen = (x for x in range(30) if x % 2 == 0)


while True:
    try:
        print(next(gen))
    except:
        break
