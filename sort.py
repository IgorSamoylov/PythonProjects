n = int(input())

inp_list = list(map(int, input().split(' ')))
    
inp_list.sort()
print(*inp_list)






n = int(input())

inp_list = []
for i in range(n):
    st = input()
    inp_list.append(st)
    
inp_list.sort()

for st in inp_list:
    print(st)



n = int(input())

inp_list = []
for i in range(n):
    st = input()
    tup = tuple(st.split(' '))
    inp_list.append(tup)
    
def compare(tupl):  # Функция сравнения возвращает второй элемент кортежа
    return tupl[1]  # Этот элемент и подаётся в функцию sorted
    
# sorted() возвращает объект упорядоченного списка!
result = sorted(inp_list, key=compare) # Можно задать функцию сравнения через kwarg key

for tup in result:
    print(*tup)
