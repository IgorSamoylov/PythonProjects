
with open("input_6_2_3.txt", "r") as f:
    res_list = f.readlines()

def compare(string):
    return len(string)

res_list.sort(key=compare)

print(res_list[-1])
