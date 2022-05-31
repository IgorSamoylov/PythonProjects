import random

N = 10_000_000
#Comp = 3

def generate_data():
    data_set = set()
    
    for i in range(N * 3):
        p = random.randint(0, N - 1)
        q = random.randint(0, N - 1)
        while q == p:
            q = random.randint(0, N - 1)
        data_set.add((p,q))
        
    return data_set


filename = "largestUF.txt"

data = f"{N}\n"
for tup in generate_data():
    data += f"{tup[0]} {tup[1]}\n"

with open(filename, "w", encoding="UTF-8") as f:
    f.write(data)
