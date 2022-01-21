
def generator(n):
    yield from range(n)
        
    
def coroutina():
    n = yield
    print(n)

gen_obj = generator(50)
cor_obj = coroutina()
next(cor_obj)

for i in range(50):
    cor_obj.send(gen_obj.__next__())
