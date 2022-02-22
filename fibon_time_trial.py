import time

def fibon(n: int):
    dp = [0] * n 
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[-1]


TESTS_N = 100
N = 20_000
result = 0

begin = time.time()

for i in range(TESTS_N):
    result = fibon(N)
    
end = time.time()

print(f"Result: {result} Time: {end - begin}  s")
