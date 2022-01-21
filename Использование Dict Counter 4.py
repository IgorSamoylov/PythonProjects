"""
Дана строка. Выведите слово, которое в этой строке встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом
(алфавитном) порядке.

Для примера:
Ввод 	Результат

apple orange banana banana orange 

	

banana
"""

import collections
inp_str = input()
inp_list = inp_str.split()

dict1 = collections.Counter(inp_list)

max_w = max(dict1.values())

inp_list.sort()

for word in inp_list:
    if dict1[word] == max_w:
        print(word)
        break
