
arr = [x + 1 for x in range(5)]

import itertools

i = 1
# Количество комбинаций для группы 3 элемента в массиве из 5 элементов  
for combination in itertools.combinations(arr, 3):
    print("Комбинация № ", i, " - ", *combination)
    i += 1
    
print(" ")

i = 1
for permutation in itertools.permutations(arr, 3):
    print("Перестановка № ", i, " - ", *permutation)
    i += 1

permutations = [x for x in itertools.permutations(arr, 3)]
print('Количество перестановок: ', len(permutations))
