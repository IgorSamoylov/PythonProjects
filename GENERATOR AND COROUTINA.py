
def factorial(n):
    i = 1
    factorial = 1
    while i < n:
        factorial *= i
        i += 1
        yield factorial


def coroutina(n):
    while True:
        print(n)
        (yield)
    

factor = factorial(5)
corout = coroutina(factor)
corout.send(next(factor))

#print(next(factor))
#print(next(factor))
#print(next(factor))
    
