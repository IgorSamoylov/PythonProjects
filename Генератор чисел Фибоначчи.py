

def fib_generator():
    n = 0
    n2 = 1
    while(True):
        summ = n + n2
        yield n
        n = n2
        n2 = summ


fib = fib_generator()
for i in range(2001):
    print(fib.__next__())
        
    
