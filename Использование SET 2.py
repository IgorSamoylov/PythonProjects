"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают
все школьники и языки, которые знает хотя бы один из школьников.

Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник. 

В первой строке выведите количество языков, которые знают все школьники. Начиная со второй
строки- список таких языков, упорядоченный по алфавиту. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков,
упорядоченный по алфавиту.

Для примера:
Ввод 	Результат

3
3
Russian
English
Japanese
2
Russian
English
1
English

	

1
English
3
English
Japanese
Russian

"""

number_s = int(input())

lang_list =[]
for i in range(number_s):
    number_lang = int(input())
    lang_set = set()
    for m in range(number_lang):
        lang = input()
        lang_set.add(lang)
    lang_list.append(lang_set)

#print(*lang_list)
    
common_set = set(lang_list[0])
for lang_set in lang_list:
    common_set &= lang_set
    
print(len(common_set))
common_list = list(common_set)
common_list.sort()
for lang in common_list:
    print(lang)
  
#print(*lang_list)

common_set = set()
for lang_set in lang_list:
    common_set |= lang_set
    
print(len(common_set))
common_list = list(common_set)
common_list.sort()
for lang in common_list:
    print(lang)  
