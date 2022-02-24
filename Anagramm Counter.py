
from collections import Counter


def anagrammCount(query: list, dictionary: list) -> list:

    result = []
    
    for q in query:
        q_counter = Counter(q)
        n = 0
        for d in dictionary:
            if len(q) == len(d):
                d_counter = Counter(d)
                print(d_counter)
                if q_counter == d_counter:
                    n += 1
                    print('Found!', n)
                    
        result.append(n)

    return result


query = ['aba', 'cat', 'wolf', 'a']
dictionary = ['baa', 'aab', 'tac', 'hghgh', 'ttc', 'a']
result = anagrammCount(query, dictionary)
print(result)
                
