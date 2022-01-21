"""
На вход подается строка. Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Для примера:
Ввод 	Результат

one two one tho three  

	

0 0 1 0 0 
"""


str_inp = input()

inp_list = str_inp.split()

word_dict = {}
result = []
for word in inp_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 0
    result.append(word_dict[word])
        
    
print(*result)
