data_list = [1, 3, 6, 10, 15]

#n = int(input())
#data_list = []

#inp_str = input()
#data_list = [x for x in map(int, inp_str.split(' '))]
#print(data_list)

i = len(data_list)
while i < 2000001:
    collision_set = set()
    for x in data_list:
        result = x % i
        if result in collision_set:
            break
        else:
            collision_set.add(result)
# Если вышли из for'а без брейка, значит для всех элементов массива
# существует только одно значение mod i, а значит мы уже нашли минимальное,
# следовательно - выход
    else:  
        break
    i += 1

print(i)
