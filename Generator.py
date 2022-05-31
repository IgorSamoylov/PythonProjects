

def Generator(n: int):
    
    result = n
    while result < 1000:
        result *= n
        yield result
    # Для цикла for StopIteration должен быть возвращен return'ом, а не вызван raise!
    return StopIteration  


gen = Generator(3)

for x in gen:
    print(x)


gen2 = Generator(2)

print(next(gen2))
print(gen2.send(20))
gen.close()


