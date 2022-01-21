MAX_INT = 2_000_000_000

data = [1,1,3,2,5,3,1,1,5,1,1,1,1,3]

DP = [MAX_INT for i in range(len(data))]
DP[0] = 0

for pos in range(1, len(DP)): # Перебираем DP список
    for i in range(0, pos):     # Перебираем входной список
        print(f'pos={pos} i = {i} data[i]={data[i]}')
        if i + data[i] >= pos:
            DP[pos] = min(DP[pos], 1 + DP[i])
            print(DP[pos], 1 + DP[i])
        


print(DP)
print(f'Последнего элемента списка можно достичь за {DP[-1]} прыжков')
