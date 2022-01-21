def myPow(x: float, n: int) -> float:
        if n == 0:
                return 0
        if n == 1:
                return x
          
        if n < 0:
                return 1 / myPow(x, -n) #так можно инвертировать число по знаку
        
        return myPow(x * x, n // 2) * (x * (n % 2) or 1)


print(myPow(2.0, 10))

print(myPow(2.1, 3))

print(myPow(2.0, -2))

#print(myPow(2, 214748364)) 
