
def createGenerator(i) :
    while i  < 100:
        yield i  # здесь функция ставится на паузу, возвращается значение перем. справа от yield
        i += 1   # при следующем вызове цикл продолжается дальше, а затем - с начала функции

mygenerator = createGenerator(10) # создаём генератор. Аргумент функции передаётся один раз!
print(mygenerator) # mygenerator является объектом!

# Объект генератора является iterable и имеет метод __next__(), этот метод может вызывать
# цикл for
for x in mygenerator:
    print(x)


