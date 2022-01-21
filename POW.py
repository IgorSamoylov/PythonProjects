def myPow(x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n > 0:
            return x * myPow(x, n - 1)
        if n < 0:
            return 1 / x * myPow(x, n + 1)



print(myPow(2.0, 10))

print(myPow(2.1, 3))

print(myPow(2.0, -2))

print(myPow(0.00001, 2147483647)) 
