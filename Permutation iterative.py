


def permutations_iterative(s: list):
    p = [0 for _ in s]
    i = 1
    result = set()

    while i < len(s):
        if p[i] < i:
            j = 0 if i % 2 == 0 else p[i]
            s[i], s[j] = s[j], s[i]
            p[i] += 1
            i = 1
            if tuple(s) not in result: 
                result.add(tuple(s))
        else:
            p[i] = 0
            i += 1
            
    return result

#s = [1, 2, 3, 4]
s = list("barsik")
for i, perm in enumerate(permutations_iterative(s)):
    print(i + 1, perm)
