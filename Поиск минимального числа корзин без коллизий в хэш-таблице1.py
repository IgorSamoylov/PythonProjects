data_list = [1, 3, 6, 10, 15]

#n = int(input())
#data_list = []

#inp_str = input()
#data_list = [x for x in map(int, inp_str.split(' '))]
#print(data_list)

i = len(data_list)

mod_list = []
for x in data_list:
    mod_list.append(x % i)
        
mod_set = set()
problem_list = []
for x in data_list:
    mod = x % i
    if mod in mod_set:
        for index, founded_mods in enumerate(mod_list):
            if founded_mods == mod: 
                problem_list.append(data_list[index])
    else:
        mod_set.add(mod)

#print(problem_list)

while i < 2_000_001:
    temp_mod_set = set()
    for x in problem_list:
        mod = x % i
        if mod in temp_mod_set:
            break
        else:
            temp_mod_set.add(mod)
    else:
        mod_set_2 = set()
        for x in data_list:
            mod = x % i
            if mod in mod_set_2:
                break
            else:
                mod_set_2.add(mod)
        else:
            break
        
    i += 1
            

print(i)
