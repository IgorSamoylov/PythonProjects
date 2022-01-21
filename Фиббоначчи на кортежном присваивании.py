
def fib(n: int) -> int:
    assert n > 0

    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, (f1 + f2)
    return f1


print(fib(200))
