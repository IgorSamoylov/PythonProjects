def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


# for i in fib():
#   print(i)


def coroutine(pattern):
    print("Searching for ", pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)


cor_obj = coroutine("coroutine")
next(cor_obj)

cor_obj.send("I love you")
cor_obj.send("Don't you love me?")
cor_obj.send("I love coroutines instead!")

cor_obj.close()
