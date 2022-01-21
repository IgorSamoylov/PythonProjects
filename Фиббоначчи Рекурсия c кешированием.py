
MaxValue = 1000
F = [None] * MaxValue


def fib(n: int) -> int:
    assert 0 <= n < MaxValue, "Input number out of range"
    
    if F[n] is not None:
        return F[n]
    elif n <= 1:
        F[n] = n
        return F[n]
    F[n] = fib(n - 1) + fib(n - 2)
    return F[n]


def fib2(n: int) -> int:
    assert 0 <= n < MaxValue, "Input number out of range"
    
    if F[n] is None:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fib2(n - 1) + fib2(n - 2)
    return F[n]


print(fib2(900))
