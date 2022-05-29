
#A = [1, 2, 3, 4, 5]
A = "вася"

def permutations(iterable):
    first_item = (iterable[0], )
    lenght = len(iterable)
    if length == 1:
        yield first_item
        
    else:
        for perm in permutations(iterable[1:]):
            for i in range(length):
                yield perm[:i] + first_item + perm[i:]

def unique_permutations(iterable):
    return list(set(permutations(iterable)))
                
#print(list(map(list, unique_permutations([1,1,1,0]))))
#print([''.join(x) for x in unique_permutations("вася")])            
        
            
for i, perm in enumerate(unique_permutations(A)):             
    print(i + 1, perm)





def factorial(n: int):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a
